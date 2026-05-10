from sqlalchemy import inspect
from app.database import engine

def get_database_schema():

    inspector = inspect(engine)

    schema = {}

    tables = inspector.get_table_names()

    for table in tables:

        columns = inspector.get_columns(table)

        schema[table] = [
            column["name"]
            for column in columns
        ]

    return schema


def format_schema_for_prompt():

    schema = get_database_schema()

    formatted_schema = ""

    for table, columns in schema.items():

        formatted_schema += f"\nTable: {table}\n"

        formatted_schema += "Columns:\n"

        for column in columns:
            formatted_schema += f"- {column}\n"

    return formatted_schema
from sqlalchemy import inspect
from app.database import engine

def get_database_schema():
    inspector = inspect(engine)

    schema = {}

    tables = inspector.get_table_names()

    for table in tables:
        columns = inspector.get_columns(table)

        schema[table] = [
            {
                "name": column["name"],
                "type": str(column["type"])
            }
            for column in columns
        ]

    return schema
from app.services.schema_service import format_schema_for_prompt
from app.utils.llm import generate_completion

def generate_sql(user_question: str):

    schema_context = format_schema_for_prompt()

    prompt = f"""
You are an expert SQLite SQL generator.

Generate ONLY SQL.

Do not explain anything.

Database Schema:
{schema_context}

User Question:
{user_question}

Rules:
- Use only existing tables and columns
- Generate valid SQLite SQL
- Do not use markdown
- Return only SQL query
"""

    sql_query = generate_completion(prompt)

    return sql_query
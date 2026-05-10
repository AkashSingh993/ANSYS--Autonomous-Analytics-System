from fastapi import APIRouter
from pydantic import BaseModel

from app.services.schema_service import get_database_schema
from app.services.sql_generator import generate_sql

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.get("/schema")
def schema():
    return get_database_schema()


@router.post("/generate-sql")
def generate_sql_endpoint(request: QueryRequest):

    sql_query = generate_sql(request.question)

    return {
        "question": request.question,
        "generated_sql": sql_query
    }
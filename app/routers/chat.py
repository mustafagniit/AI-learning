from fastapi import APIRouter
from pydantic import BaseModel

from services.rag import(
    search_documents
) 

from openai import OpenAI
import os

router  = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

client = OpenAI(
    api_key=os.getenv(
        ""
    )
)


class CharRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: CharRequest):
    context = search_documents(request.question)
    prompt= f"""you are helpfull assistant. Answer only using this context:
    {context}
    Question:
    {request.question}
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return{
        "answer": response.output_text
    }

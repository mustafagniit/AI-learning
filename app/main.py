from fastapi import FastAPI
from routers import chat
from routers import upload

app = FastAPI(
    title="RAG Chatbot API"
)

app.include_router(
    upload.router
)

app.include_router(
    chat.router
)

app.get("/")
def Home():
    return{
        "message": "RAG Chabot running"
    }
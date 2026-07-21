from fastapi import FastAPI
from routers import chat
from routers import upload
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="RAG Chatbot API"
)

app.include_router(
    upload.router
)

app.include_router(
    chat.router
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get("/")
def Home():
    return FileResponse(
        BASE_DIR / "static" / "index.html"
    )

@app.get("/chatbot/v1")
def chatbot():
    return FileResponse("chatbot/v1.html")

@app.get("/chatbot/v2")
def chatbot():
    return FileResponse("chatbot/v2.html")
# app.get("/")
# def Home():
#     # return{
#     #     "message": "RAG Chabot running"
#     # }
#     return FileResponse(
#          "static/index.html"
#      )
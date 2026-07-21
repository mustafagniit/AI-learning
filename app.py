from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from chatbot import ChatBot


app = FastAPI(
    title="OpenAI Chatbot API"
)

bot = ChatBot()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

class ChatRequst(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def Home():
    return FileResponse(
        "static/index.html"
    )

@app.post("/chat", response_model=ChatResponse)
def char(requst: ChatRequst):
    try:
        answer = bot.ask(
            requst.message
        )
        return{
            "reply": answer
        }
    except Exception as e:
        print(f"CHAT ERROR: {str(e)}")
        raise
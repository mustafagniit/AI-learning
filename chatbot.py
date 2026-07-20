import os
from dotenv import load_dotenv
from  openai import OpenAI

load_dotenv()


class ChatBot:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("")
        )

        self.message=[
            {
                "role": "system",
                "content": "you are helpful assistant."
            }
        ]


    def ask(self, user_message: str):
        self.message.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = self.client.responses.create(
            model="gpt-5",
            input=self.message
        )

        assistant_reply = response.output_text

        self.message.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        return assistant_reply



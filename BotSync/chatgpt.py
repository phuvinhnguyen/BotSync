import openai
from .abstract import AbstractBot

class ChatGPTBot(AbstractBot):
    def __init__(self, token, model="gpt-4"):
        super().__init__()
        openai.api_key = token
        self.model = model

    def __run__(self, text):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": text}]
        )
        return response['choices'][0]['message']['content']
    
    def prompt(self, text):
        return text

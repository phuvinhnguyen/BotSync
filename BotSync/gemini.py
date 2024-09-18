import google.generativeai as genai
from .monitor import AbstractBot


@AbstractBot.register_class("gemini")
class GeminiBot(AbstractBot):
    def __init__(self, token, bot="gemini-1.5-flash"):
        super().__init__()
        genai.configure(api_key=token)
        self.model = genai.GenerativeModel(bot)

    def __run__(self, text):
        return self.model.generate_content(text).text

    def prompt(self, text):
        return text

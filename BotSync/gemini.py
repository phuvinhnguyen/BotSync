import google.generativeai as genai
from .monitor import AbstractBot


@AbstractBot.register_class("gemini")
class GeminiBot(AbstractBot):
    def __init__(self, token, bot="gemini-1.5-flash"):
        super().__init__()
        genai.configure(api_key=token)
        self.model = genai.GenerativeModel(bot)

    def __run__(self, text):
        for _ in range(5):
            try:
                result = self.model.generate_content(text).text
                return result
            except Exception as e:
                print(e)

        return ''

    def prompt(self, text):
        return text

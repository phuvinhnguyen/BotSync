import google.generativeai as genai
from ..monitor import AbstractBot


@AbstractBot.register_class("gemini")
class GeminiBot(AbstractBot):
    def __init__(self, token, bot="gemini-1.5-flash"):
        super().__init__()
        self.bot = bot
        self.token = token

        if isinstance(token, list):
            self.switch_between = True
            self.index = 0
            self.num_token = len(token)
            self.repeat_time = len(token) + 2
        else:
            genai.configure(api_key=token)
            self.switch_between = False
            self.model = genai.GenerativeModel(bot)
            self.repeat_time = 5

    def __run__(self, text):
        for _ in range(self.repeat_time):
            if self.switch_between:
                self.index = (self.index + 1) % self.num_token
                genai.configure(api_key=self.token[self.index])
                self.model = genai.GenerativeModel(self.bot)

            try:
                result = self.model.generate_content(text).text
                return result
            except Exception as e:
                print(e)

        return ''

    def prompt(self, text):
        return text
    

@AbstractBot.register_class("multiturn_gemini")
class MultiTurnGeminiBot(AbstractBot):
    def __init__(self, token, bot="gemini-1.5-flash"):
        super().__init__()
        self.bot = bot
        self.token = token
        self.history = []

        if isinstance(token, list):
            self.switch_between = True
            self.index = 0
            self.num_token = len(token)
            self.repeat_time = len(token) + 2
        else:
            genai.configure(api_key=token)
            self.switch_between = False
            self.model = genai.GenerativeModel(bot).start_chat(history=self.history)
            self.repeat_time = 5

    def __run__(self, text):
        for _ in range(self.repeat_time):
            if self.switch_between:
                self.index = (self.index + 1) % self.num_token
                genai.configure(api_key=self.token[self.index])
                self.model = genai.GenerativeModel(self.bot).start_chat(history=self.history)

            try:
                result = self.model.send_message(text).text
                self.history += [
                    {"role": "user", "parts": text},
                    {"role": "model", "parts": result},
                ]
                return result
            except Exception as e:
                print(e)

        return ''

    def prompt(self, text):
        return text

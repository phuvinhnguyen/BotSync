import openai
from ..monitor import AbstractBot
import base64
import io
from PIL import Image

@AbstractBot.register_class("chatgpt")
class ChatGPTBot(AbstractBot):
    def __init__(self, token, bot="gpt-4o-mini", eco=True):
        super().__init__()
        openai.api_key = token
        self.model = bot
        self.eco = eco

    def __encode_image(self, image):
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    
    def __obj2content(self, obj):
        if isinstance(obj, str):
            return {
                "type": "text",
                "text": obj,
            }
        elif isinstance(obj, Image.Image):
            if self.eco:
                obj = obj.resize(256, 256)
            return {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{self.__encode_image(obj)}"
                }
            }
    def __run__(self, text):
        content = [self.__obj2content(i) for i in text] if isinstance(text, list) else text
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            # max_tokens = 200,
        )
        return response.choices[0].message.content

    def prompt(self, text):
        return text

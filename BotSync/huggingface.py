from huggingface_hub import InferenceApi
from .monitor import AbstractBot


@AbstractBot.register_class("huggingface")
class HuggingFaceBot(AbstractBot):
    def __init__(self, token, model="gpt2"):
        super().__init__()
        self.api = InferenceApi(repo_id=model, token=token)

    def __run__(self, text):
        response = self.api(inputs=text)
        return response[0]['generated_text']

    def prompt(self, text):
        return text

import time
from .gemini import *
from .chatgpt import *
from .huggingface import *


class AbstractBot:
    def __run__(self, text):
        raise NotImplementedError

    def generate(self, text):
        return self.__run__(self.prompt(text))

    def prompt(self, text):
        raise NotImplementedError

    def run_batch(self, texts, delay=10):
        results = []
        for text in texts:
            output = self.generate(text)
            results.append((text, output))
            time.sleep(delay)

        return results

    def run_file(self, filename, delay=5):
        with open(filename, 'r') as f:
            texts = f.readlines()

        return self.run_batch(texts, delay)

    _registry = {}

    @classmethod
    def register_class(cls, key):
        """Decorator to register a new child class."""
        def wrapper(subclass):
            cls._registry[key] = subclass
            return subclass
        return wrapper

    @classmethod
    def create_instance(cls, key, *args, **kwargs):
        """Factory method to create an instance of a registered child class."""
        if key not in cls._registry:
            raise ValueError(f"Class with key '{key}' is not registered.")
        return cls._registry[key](*args, **kwargs)


class MonitorBot:
    def __init__(self, bot_code, *args, **kwargs):
        self.bot = AbstractBot.create_instance(bot_code, *args, **kwargs)

    def switch(self, bot_code, *args, **kwargs):
        self.bot = AbstractBot.create_instance(bot_code, *args, **kwargs)

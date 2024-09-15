import time

class AbstractBot:
    def __run__(self, text):
        raise NotImplementedError
    
    def generate(self, text):
        return self.__run__(self.prompt(text))
    
    def prompt(self, text):
        raise NotImplementedError
    
    def run_batch(self, texts, delay=5):
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
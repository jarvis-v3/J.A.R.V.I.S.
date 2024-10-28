# blackboxai.py
from blackboxai import BlackBoxAI

class AIResponder:
    def __init__(self):
        self.ai = BlackBoxAI()

    def get_response(self, user_input):
        response = self.ai.chat(user_input)
        return response

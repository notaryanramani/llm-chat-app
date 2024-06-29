import os 
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = 'YOUR_API_KEY'

class GeminiModel:
    def __init__(self):
        self.genai = genai
        self.genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        
    def init_model(self):
        self.model = self.genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat(history=[])
    
    def get_response(self, prompt):
        response = self.chat.send_message(prompt, stream=True)
        return response

    


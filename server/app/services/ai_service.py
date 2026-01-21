import google.generativeai as genai
from ..core.config import settings

class AIService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None

    async def generate_response(self, prompt: str) -> str:
        if not self.model:
            return "AI service not configured. Please add GEMINI_API_KEY."
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error calling Gemini: {str(e)}"

ai_service = AIService()

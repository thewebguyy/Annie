from typing import List, Dict
import random

from .ai_service import ai_service

class HookService:
    @staticmethod
    def analyze_hook(text: str) -> Dict:
        """
        Analyzes the first 30 seconds (approx 75 words) for engagement.
        """
        first_part = " ".join(text.split()[:75])
        
        # Mock scoring logic
        score = 80
        if "?" in first_part: score += 5
        if "!" in first_part: score += 5
        if len(first_part.split()) < 20: score -= 10
        
        return {
            "score": min(100, score),
            "heatmap": [random.randint(40, 95) for _ in range(10)],
            "feedback": "Strong opening, but consider adding a question for higher curiosity."
        }

    @staticmethod
    async def generate_variants(base_hook: str, platform: str) -> List[str]:
        """
        Generates platform-specific hook variants using Gemini.
        """
        prompt = f"""
        Act as a professional scriptwriter and retention engineer.
        Generate 3 high-engagement hook variants for the following base hook:
        "{base_hook}"
        Target Platform: {platform}
        Focus on psychological triggers: Curiosity, Fear of Missing Out, or Desire.
        Output as a numbered list.
        """
        response = await ai_service.generate_response(prompt)
        # Parse numbered list
        import re
        variants = re.findall(r'\d+\.\s*(.*)', response)
        return variants if variants else [base_hook]

hook_service = HookService()

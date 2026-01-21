from typing import List, Dict

from .ai_service import ai_service

class ReframerService:
    @staticmethod
    async def reframe_script(script_text: str, target_platforms: List[str]) -> Dict:
        """
        Atomizes long-form content into platform-native formats using Gemini.
        """
        results = {}
        for platform in target_platforms:
            prompt = f"""
            Act as a social media strategist and scriptwriter.
            Reframe the following long-form script for {platform}.
            Script Content: "{script_text}"
            
            Rules:
            - TikTok: Focus on speed, 3 main points, vertical hooks.
            - X: Format as a high-engagement thread (numbered).
            - Instagram Reels: Educational and visual-first.
            
            Provide only the reframed script.
            """
            reframed = await ai_service.generate_response(prompt)
            results[platform] = reframed
            
        return results

reframer_service = ReframerService()

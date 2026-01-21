import re
from typing import List, Dict
import spacy

# Load English model for NLP tasks
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # Fallback if not installed yet
    nlp = None

class RetentionService:
    WORDS_PER_MINUTE = 150
    DEAD_ZONE_THRESHOLD_SEC = 20 # 20 seconds threshold for visual cues
    
    @staticmethod
    def analyze_pacing(text: str) -> Dict:
        """
        Scans script for word density and flags Dead Zones.
        """
        # Split text into segments based on visual cues or paragraph breaks
        # Visual cues are often bracketed: [Visual: Tracking shot] or (B-roll: ...)
        segments = re.split(r'(\[.*?\]|\(.*?\))', text)
        
        results = []
        current_time = 0
        
        for i, segment in enumerate(segments):
            is_cue = bool(re.match(r'\[.*?\]|\(.*?\)', segment))
            word_count = len(segment.split())
            duration = (word_count / RetentionService.WORDS_PER_MINUTE) * 60
            
            segment_data = {
                "text": segment,
                "is_cue": is_cue,
                "duration": duration,
                "start_time": current_time,
                "end_time": current_time + duration
            }
            
            if not is_cue and duration > RetentionService.DEAD_ZONE_THRESHOLD_SEC:
                segment_data["risk"] = "High"
                segment_data["alert"] = f"Dead Zone detected: {duration:.1f}s without visual cue."
                segment_data["suggestion"] = RetentionService.generate_interrupt_suggestion(segment)
            
            results.append(segment_data)
            current_time += duration
            
        return {
            "segments": results,
            "total_duration": current_time,
            "overall_risk_score": RetentionService.calculate_risk_score(results)
        }

    @staticmethod
    def generate_interrupt_suggestion(text_block: str) -> str:
        """
        Suggests pattern interrupts (B-roll, zooms, SFX) based on content.
        """
        # Simple rule-based suggestion for now
        keywords = {
            "car": "B-roll of moving vehicle / wheel close-up",
            "tech": "Motion graphic overlay of data/code",
            "future": "Futuristic soundscape transition + Zoom in",
            "money": "Sound effect: Cash register / Graphic of rising chart",
            "people": "Cut to reaction shot or street interview B-roll"
        }
        
        for key, suggestion in keywords.items():
            if key in text_block.lower():
                return suggestion
        
        return "Insert B-Roll or change camera angle (Zoom/Pan)"

    @staticmethod
    def calculate_risk_score(segments: List[Dict]) -> float:
        """
        Simple predictive score based on dead zone count and duration.
        """
        total_duration = sum(s["duration"] for s in segments)
        if total_duration == 0: return 0
        
        dead_zone_duration = sum(s["duration"] for s in segments if s.get("risk") == "High")
        score = 100 - (dead_zone_duration / total_duration * 100)
        return round(max(0, score), 1)

    @staticmethod
    def generate_chapters(text: str) -> List[Dict]:
        """
        Automatic chaptering using semantic beats.
        """
        if not nlp: return []
        
        doc = nlp(text)
        chapters = []
        # Logic to find "pivots" or new topics
        # For now, use Noun Chunk counts or heading identification
        # Placeholder: Every 200 words is a new chapter beat
        words = text.split()
        for i in range(0, len(words), 200):
            beat_text = " ".join(words[i:i+5]) + "..."
            chapters.append({
                "timestamp": (i / RetentionService.WORDS_PER_MINUTE) * 60,
                "title": f"Section: {beat_text}"
            })
        return chapters

retention_service = RetentionService()

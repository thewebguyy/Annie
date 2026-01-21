import os
from typing import List, Dict, Optional
import numpy as np
from PyPDF2 import PdfReader
from docx import Document
from ..core.config import settings

class VoiceService:
    def __init__(self):
        # In a real app, we'd initialize Pinecone/Milvus here
        self.personas = {} # Mock storage for personas: {persona_id: [vectors]}

    def extract_text(self, file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self._extract_pdf(file_path)
        elif ext == '.docx':
            return self._extract_docx(file_path)
        elif ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def _extract_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def _extract_docx(self, file_path: str) -> str:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    def create_persona(self, persona_id: str, texts: List[str]):
        """
        Processes texts to create a Brand Voice Persona using embeddings.
        """
        # Placeholder for actual embedding logic
        # embeddings = [get_embedding(t) for t in texts]
        # self.personas[persona_id] = embeddings
        self.personas[persona_id] = ["Mock Vector Data"]
        return {"status": "trained", "persona_id": persona_id}

    def audit_script(self, script_text: str, persona_id: str) -> Dict:
        """
        Lints script for brand consistency using cosine similarity.
        """
        # Placeholder: Identify "Brand Keywords" and "Tone"
        # In production, use Sentence Transformers to compare script chunks 
        # against the Persona Vector Space.
        
        drift_score = 0.15 # Low drift
        suggestions = []
        
        # Simple rule-based audit for demo
        if "synergy" in script_text.lower():
            suggestions.append({
                "original": "synergy",
                "suggested": "collaboration",
                "reason": "Avoid corporate jargon for this persona."
            })
            drift_score += 0.1
            
        return {
            "drift_detected": drift_score > 0.2,
            "drift_score": drift_score,
            "suggestions": suggestions
        }

voice_service = VoiceService()

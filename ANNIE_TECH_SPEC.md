# Annie: Technical Specification Document (v1.0)
## 2026 Creative Operating System for Scriptwriters

**Date**: January 21, 2026
**Status**: Draft Specification
**Confidentiality**: Professional / Internal

---

## 1. Executive Summary
Annie is a "Retention Engineering" platform designed to transform the workflow of professional scriptwriters. Unlike traditional word processors, Annie treats scripts as data-driven engagement assets. It integrates real-time AI analytics, brand voice cloning, and multi-platform reframing to reduce production time by 60% and boost viewer retention (APV) by 20%.

---

## 2. Technical Architecture

### 2.1 Backend (Python/Node.js Hybrid)
- **API Layer**: FastAPI (Python) for high-performance AI orchestration.
- **Workflow Engine**: LangGraph/LangChain for agentic state management.
- **Task Queue**: Celery with Redis for asynchronous long-running AI tasks (e.g., full script reframing).
- **Search & RAG**: Pinecone or Milvus for the **Voice Vault (RAG)** and **Research Autopilot**.

### 2.2 Frontend (React & Modern UI)
- **Framework**: React 19+ with Vite.
- **State Management**: Zustand (for script state) and TanStack Query (for server state).
- **Editor**: Lexical or TipTap (Prosemirror-based) for high extensibility and AI-marker injection.
- **Styling**: Vanilla CSS or Tailwind (based on user preference), following "Focused Minimalism".
- **Visuals**: Framer Motion for micro-animations and "Lens" transitions.

### 2.3 AI Stack
- **Primary Models**: Claude 3.5 Sonnet (Coding/Logic), Gemini 1.5 Pro (Long Context/Research), GPT-4o (General Purpose).
- **Embedding Models**: OpenAI `text-embedding-3-small` or HuggingFace local models for sensitive IP.
- **Image/Video**: Stable Diffusion XL / Runway Gen-3 (for Pre-Viz).

---

## 3. API Blueprint (OpenAPI v3.1)

### 3.1 AI Retention Engine
- `POST /api/v1/analyze/retention`
    - **Description**: Scans script for Word Density vs. Visual Cues.
    - **Input**: `{ "script_body": "string", "target_duration": "int" }`
    - **Output**: `{ "risk_score": 0.85, "dead_zones": [{ "start": 45, "end": 62, "reason": "Monologue too long" }] }`

### 3.2 Brand Voice Vault
- `POST /api/v1/voice/train`
    - **Description**: Clones a brand persona from uploaded assets.
- `GET /api/v1/voice/audit`
    - **Description**: Real-time linter for brand consistency.
    - **Output**: `{ "drift_detected": true, "suggestions": [{ "text": "Leverage", "replace_with": "Use", "reason": "Too corporate for Gen-Z persona" }] }`

### 3.3 Hook Intelligence
- `GET /api/v1/hooks/predict`
    - **Description**: Heatmap prediction and variant generation.

---

## 4. UI/UX Wireframes (ASCII)

### 4.1 Main Workspace
```text
+-----------------------------------------------------------------------+
|  [A] Annie | [File] [Edit] [View] [Tools]                [User Profile]|
+------------+---------------------------------------------+------------+
| [L] LENSES | [C] CENTRAL WRITING AREA                    | [R] ANALYTICS|
|            |                                             |            |
| > Pacing   |  # The Future of Energy                     |  RETENTION |
|   Voice    |                                             |  [====--]  |
|   Research |  "In a world where energy is everything..." |  Risk: MED |
|   Reframer |  [AI SUGGESTION: ADD B-ROLL HERE]           |            |
|            |                                             |  HOOK SCORE|
|            |  The car hums as it glides over...          |  [92/100]  |
|            |                                             |            |
|            |                                             |  VOICE: OK |
|            |                                             |            |
+------------+---------------------------------------------+------------+
| [Timeline View: [---Hook---][---Mid-Story---][---CTA---] ]            |
+-----------------------------------------------------------------------+
```

---

## 5. Core Feature Specifications

### 5.1 Real-Time Visual Pacing Tracker (Level 1)
- **Logic**: Calculates "Silence-to-Action" ratio.
- **Constraint**: Flags any segment > 20 seconds without a defined visual cue (B-Roll, Motion Graphic, Zoom).
- **Action**: Auto-suggests "Interrupts" based on semantic context of the text.

### 5.2 Voice Vault & Brand Audit (Level 2)
- **RAG Implementation**: Stores chunks of "Approved Scripts" in a vector database.
- **Linter**: Runs a cosine similarity check between the current draft and the persona vector.
- **Drift Alert**: If similarity drops below 0.75, the sidebar turns amber.

---

## 6. Sample Implementation (Python - Retention Analyzer)

```python
import spacy
from typing import List, Dict

nlp = spacy.load("en_core_web_sm")

def analyze_retention_risk(script_text: str) -> List[Dict]:
    doc = nlp(script_text)
    risks = []
    current_word_count = 0
    # Threshold: Visual interrupts needed every 150 words (approx 60s)
    INTERRUPT_THRESHOLD = 50 
    
    sections = script_text.split("\n\n")
    for sec in sections:
        words = len(sec.split())
        if words > INTERRUPT_THRESHOLD and "[Visual]" not in sec:
            risks.append({
                "type": "Dead Zone",
                "content": sec[:30] + "...",
                "severity": "High",
                "suggestion": "Insert B-Roll or Visual Hook"
            })
    return risks
```

---

## 7. Compliance & Standards
- **GDPR/NDPR**: All "Voice Persona" data is encrypted at rest (AES-256). "Zero-Retention" mode for corporate client IP.
- **Accessibility**: ARIA-labeled components; High Contrast Mode (WCAG 2.1 AA).
- **Security**: ISO 27001 compliant SOC 2 Type II environment.

---

## 8. Demo User Flow Script
1. **Onboarding**: Aisha (Writer) uploads 3 Tesla scripts. Annie creates the "Cyber-Punk Corporate" voice model.
2. **Drafting**: Aisha types a new intro. The **Hook Intelligence System** flags the hook as "Generic".
3. **Pacing Improvement**: Aisha clicks "Auto-Insert Cues". Annie adds `[Visual: Tracking shot of Model 3]` at the 15s mark.
4. **Reframing**: Aisha clicks "Multi-Platform Reframer". Annie generates a TikTok script focusing on "3 Crazy Tesla Facts" from the main script.
5. **Vibe Check**: The **Emotional Arc Visualization** shows a drop in tension during the middle section; Aisha tightens the dialogue.

---

## 9. Success Metrics (KPIs)
- **Drafting Speed**: Internal target: 1 script (10 mins) drafted in < 4 hours.
- **Engagement**: 20% increase in 1st 30-sec retention vs. baseline scripts.
- **Repurposing**: < 2 minutes to generate 5 social threads.

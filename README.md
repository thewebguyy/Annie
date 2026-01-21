# Annie: 2026 Creative Operating System

Annie is a high-performance, AI-native workspace for professional scriptwriters, brand managers, and social-first agencies. It transforms scriptwriting into a data-driven "Retention Engineering" process.

## 🌟 Core Features

### Level 1: Retention Engine
- **Visual Pacing Tracker**: Real-time scan of word density vs. visual cues.
- **Dead Zone Alerts**: Flags segments over 20s without pattern interrupts.
- **Predictive APV Score**: Estimates viewer retention based on script structure.

### Level 2: Voice Vault
- **Voice Persona Cloning**: Train on 5+ scripts to capture unique brand voices.
- **Brand Audit Linter**: Real-time checking for tone drift and inconsistent language.

### Level 3: Hook Intelligence
- **Engagement Heatmaps**: Predicts the first 30 seconds of performance.
- **AI Hook Variants**: Generates platform-specific hooks (YouTube, TikTok, X).

### Level 4: Research Autopilot
- **2026 Fact Verification**: Real-time trend integration and citation management.
- **AEO Optimization**: Structures output for Answer Engine Optimization.

### Level 5: Multi-Platform Reframer
- **AI Content Atomization**: Turns 1 long-form script into 10+ social assets instantly.

---

## 🛠 Tech Stack
- **Frontend**: React 19, Zustand, Lucide, Framer Motion, Vanilla CSS.
- **Backend**: FastAPI, LangChain, Motor (MongoDB), SQLAlchemy (PostgreSQL).
- **AI**: Google Gemini 1.5 Pro/Flash, OpenAI Embeddings.
- **Infrastructure**: Docker, Redis, Celery.

---

## 🚀 Getting Started

1.  **Clone the repo**.
2.  **Infrastructure**: Run `docker-compose up -d` to start PostgreSQL, MongoDB, and Redis.
3.  **Backend**:
    ```bash
    cd server
    pip install -r requirements.txt
    uvicorn app.main:app --reload
    ```
4.  **Frontend**:
    ```bash
    cd client
    npm install
    npm run dev
    ```

## 🔒 Security & Compliance
- **GDPR / NDPR Compliant**.
- **AES-256 Encryption** for all Script IP.
- **Zero-Retention Mode** available for corporate clients.

---
Built for the 2026 Creator Economy.

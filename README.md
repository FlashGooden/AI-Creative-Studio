# CreativeFlow AI

A comprehensive multi-modal AI content generation platform that combines text, image, and audio processing to create complete creative projects.

## Features

- **Story Generator**: Complete stories with illustrations and narration
- **Social Media Campaigns**: Full campaign packages with posts, images, and copy
- **Presentation Builder**: AI-powered slide decks with visuals and speaker notes
- **Podcast Generator**: Scripts with AI voice narration and background music
- **Creative Writing Assistant**: Collaborative writing with AI suggestions

## Tech Stack

- **Frontend**: React 18 + TypeScript + Tailwind CSS + Framer Motion
- **Backend**: Python + FastAPI + SQLAlchemy + Redis
- **AI Services**: OpenAI (GPT-4, DALL-E 3, Whisper), ElevenLabs, Stability AI
- **Database**: PostgreSQL + Redis
- **Deployment**: Docker + AWS/Railway + S3

## Development Setup

### Prerequisites

- Node.js 18+
- Python 3.9+
- Docker & Docker Compose
- PostgreSQL
- Redis

### Quick Start

1. Clone the repository
2. Copy environment files: `cp .env.example .env`
3. Start services: `docker-compose up -d`
4. Install dependencies and run:

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm start
```

## Project Structure

```
├── backend/          # FastAPI backend
├── frontend/         # React frontend
├── docker-compose.yml
└── README.md
```

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation.
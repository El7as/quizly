# Quizly Backend

Quizly is a Django‑based backend application that automatically generates quizzes from YouTube videos.
Users authenticate, submit a YouTube URL, and the system extracts the transcript, processes it with Google Gemini, and returns a fully structured quiz with questions, options, and correct answers.

---

## Features

User Authentication
    - Registration & login using Django REST Framework
    - JWT authentication with HTTP‑only cookies

YouTube Transcript Extraction
    - Audio download via yt-dlp
    - Local transcription using Whisper

AI‑Generated Quizzes
    - Powered by Google Gemini (Flash 3.5)
    - 10 questions per quiz
    - 4 answer options per question
    - Correct answer automatically assigned

Quiz Management
    - Create quizzes from YouTube URLs
    - List all quizzes belonging to the authenticated user
    - Retrieve, update, and delete quizzes
    - Nested serialization (Quiz → Questions → Options)

Clean, modular architecture
    - auth_app for authentication
    - quizly_app for quiz logic
    - utils for AI and transcript processing

---

## Requirements

    - Python 3.10+

    - Django 5+

    - Django REST Framework

    - yt-dlp

    - ffmpeg (must be installed globally)

    - Whisper (local)

    - Google Gemini API key

Environment Variables
    Create a .env file in the project root:


## Environment Variables
GEMINI_API_KEY=your_api_key_here


## Installation

```bash
git clone <your-repo-url>


cd project


python -m venv env


source venv/bin/activate # Windows: venv\Scripts\activate

pip install -r requirements.txt


python manage.py makemigrations


python manage.py migrate


python manage.py runserver

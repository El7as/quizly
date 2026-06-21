Features


User Authentication
    Registration & login using Django REST Framework
    JWT authentication with HTTP‑only cookies

YouTube Transcript Extraction
    Audio download via yt-dlp
    Local transcription using Whisper

AI‑Generated Quizzes
    Powered by Google Gemini (Flash 3.5)
    10 questions per quiz
    4 answer options per question
    Correct answer automatically assigned

Quiz Management
    Create quizzes from YouTube URLs
    List all quizzes belonging to the authenticated user
    Retrieve, update, and delete quizzes
    Nested serialization (Quiz → Questions → Options)

Clean, modular architecture
    auth_app for authentication
    quizly_app for quiz logic
    utils for AI and transcript processing


Requirements
    Python 3.10+
    Django 5+
    Django REST Framework
    yt-dlp
    ffmpeg (must be installed globally)
    Whisper (local)
    Google Gemini API key


Environment Variables
    Create a .env file in the project root:


Installation
    git clone <your-repo-url>
    cd project
    python -m venv env
    source venv/bin/activate  # Windows: venv\Scripts\activate
<<<<<<< HEAD
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
=======
    pip install -r 

    
>>>>>>> 7ca693f1f7739026599b5ba2bdfde72a2c2845e7

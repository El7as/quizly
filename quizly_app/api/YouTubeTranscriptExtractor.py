import re
from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


class YouTubeTranscriptExtractor:

    def extract_video_id(self, url: str) -> str:
        patterns = [
            r"v=([a-zA-Z0-9_-]{11})",
            r"youtu\.be/([a-zA-Z0-9_-]{11})",
            r"youtube\.com/embed/([a-zA-Z0-9_-]{11})"
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        raise Exception("Konnte keine gültige YouTube-Video-ID extrahieren.")

    def get_transcript(self, youtube_url: str) -> str:
        video_id = self.extract_video_id(youtube_url)

        try:
            api = YouTubeTranscriptApi()
            transcript_list = api.fetch(video_id, languages=['de', 'de-DE', 'en'])

            # Hier: Zugriff auf Attribute statt Dictionary-Schlüssel
            transcript_text = " ".join([item.text for item in transcript_list])
            return transcript_text

        except TranscriptsDisabled:
            raise Exception("Dieses Video hat keine Untertitel (TranscriptsDisabled).")

        except NoTranscriptFound:
            raise Exception("Für dieses Video wurden keine Untertitel gefunden.")

        except Exception as e:
            raise Exception(f"Fehler beim Abrufen des Transkripts: {str(e)}")

# import os
# import yt_dlp
# import uuid
# import tempfile
# import subprocess


# class YouTubeAudioExtractor:
#     def download_audio(self, youtube_url: str):
#         tmp_basename = f'{uuid.uuid4().hex}'
#         tmp_dir = tempfile.gettempdir()
#         tmp_filename = os.path.join(tmp_dir, tmp_basename)

#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'outtmpl': tmp_filename,
#             'quiet': True,
#             'noplaylist': True,
#             'force_ipv4': True,
           
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192'}],

#             'http_headers': {'User-Agent': 'Mozilla/5.0'},
#             'js_runtimes':{'node': {'path': 'C:\\Program Files\\nodejs\\node.exe'}},
#             'remote_components': ['ejs:github']}

#             # 'skip_download': True,
#             # 'writesubtitles': True,
#             # 'writeautomaticsub': True,
#             # 'subtitleslangs': ['de'],
#             # 'outtmpl': tmp_filename + '.%(ext)s'}

        
#         try:
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([youtube_url])
#         except Exception as e:
#             raise Exception(f'Fehler beim Herunterladen der Audio: {str(e)}')
        
#         # if not os.path.exists(tmp_filename):
#         #     raise Exception('Audio-Datei wurde nicht erstellt')
        
#         # return tmp_filename

#         for ext in ['mp3', 'm4a', 'webm']:
#             candidate = os.path.join(tmp_dir, f'{tmp_basename}.{ext}')
#             if os.path.exists(candidate):
#                 return candidate
            
#             raise Exception('Audio-Datei wurde nicht erstellt')

#         #     raise Exception(f'Fehler beim Herunterladen der Audio: {str(e)}')
#         # if not os.path.exists(tmp_filename):
#         #     raise FileNotFoundError('Audio-Datei wurde nicht erstellt.')
#         # return tmp_filename



#     def transcribe_audio_whisper_cli(self, audio_path: str):

#         try:
#             result = subprocess.run(['whisper', audio_path, '--model', 'base', '--language', 'de', '--fp16', 'False'],
#                                     capture_output=True, text=True)
            
#             transcript_file = audio_path + '.txt'

#             if not os.path.exists(transcript_file):
#                 raise Exception('Whisper hat keine Transkriptdatei erzeugt')
            
#             with open(transcript_file, 'r', encoding='utf-8') as f:
#                 return f.read()
    
#         except Exception as e:
#             raise Exception(f'Whisper CLI Fehler: {str(e)}')
        

#     def generate_transcript_from_youtube_url(self, url: str):
#         audio_path = self.download_audio(url)

#         # audio_path = self.download_audio(url)
#         transcript = self.transcribe_audio_whisper_cli(audio_path)
#         return transcript
    

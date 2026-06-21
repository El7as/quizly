from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from ..models import Quiz, Question, Option

from .serializers import QuizSerializer, QuizListSerializer

# from .youtube_audio_extractor import YouTubeAudioExtractor
from .YouTubeTranscriptExtractor import YouTubeTranscriptExtractor
from .gemini_quiz_generator import GeminiQuizGenerator



class QuizView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        quizzes = Quiz.objects.filter(user=request.user)
        serializer = QuizListSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        video_url = request.data.get('url')
        if not video_url or not ('youtube.com' in video_url or 'youtu.be' in video_url):
            return Response({'detail': 'Ungültige URL oder Anfragedaten.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            # Audio & Transkript erzeugen
            extractor = YouTubeTranscriptExtractor() # YouTubeAudioExtractor
            transcript = extractor.get_transcript(video_url)

            # Quizfragen generieren
            generator = GeminiQuizGenerator()
            quiz_data = generator.generate_quiz(transcript)

            # Quiz speichern
            quiz = Quiz.objects.create(user=request.user, title='Automatisch generiertes Quiz',
                                       description='Erstellt aus YouTube-Video', url=video_url)
            
            # Fragen speichern
            for q in quiz_data:
                question = Question.objects.create(quiz=quiz, text=q['question'])
                for opt in q['options']:
                    Option.objects.create(question=question, text=opt, is_correct=(opt == q['answer']))

            serializer = QuizSerializer(quiz)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

                
    #     quiz = Quiz.objects.create(user=request.user, title='Ouiz Title', description='Quiz Description', url=video_url)
    #     question = Question.objects.create(quiz=quiz, text='Question 1')
    #     Option.objects.create(question=question, text='Option A', is_correct=True)
    #     Option.objects.create(question=question, text='Option B', is_correct=True)
    #     Option.objects.create(question=question, text='Option C', is_correct=True)
    #     Option.objects.create(question=question, text='Option D', is_correct=True)

    #     serializer = QuizSerializer(quiz)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)



class QuizDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self, pk):
        try:
            return Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return None
        

    def get(self, request, pk):
        quiz = self.get_object(pk)

        if quiz is None:
            return Response({'detail': 'Quiz nicht gefunden'}, status=status.HTTP_404_NOT_FOUND)

        if quiz.user != request.user:
            return Response({'detail': 'Keine Berechtigung'}, status=status.HTTP_403_FORBIDDEN)

        serializer = QuizListSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):
        quiz = self.get_object(pk)

        if quiz is None:
            return Response({'detail': 'Quiz nicht gefunden'}, status=status.HTTP_404_NOT_FOUND)
        
        if quiz.user != request.user:
            return Response({'detail': 'Keine Berechtigung'}, status=status.HTTP_403_FORBIDDEN)

        title = request.data.get('title')
        description = request.data.get('description')

        if not title or not description:
            return Response({'detail': 'title und description müssen angegeben werden'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = QuizListSerializer(quiz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        quiz = self.get_object(pk)

        if quiz is None:
            return Response({'detail': 'Quiz nicht gefunden'}, status=status.HTTP_404_NOT_FOUND)
        
        if quiz.user != request.user:
            return Response({'detail': 'Keine Berechtigung'}, status=status.HTTP_403_FORBIDDEN)
        
        quiz.delete()
        return Response(status=status.HTTP_200_OK)
    


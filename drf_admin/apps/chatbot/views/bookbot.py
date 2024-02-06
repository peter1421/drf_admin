from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chatbot.models import StudentBookBot
from chatbot.serializers.bookbot import StudentBookBotSerializer

class StudentBookBotView(APIView):
    ## 取得當前的機器人ID
    def get(self, request, format=None):
        try:
            student = request.query_params.get('student')
            book = request.query_params.get('book')
            student_book_bot = StudentBookBot.objects.get(student=student, book=book)
            serializer = StudentBookBotSerializer(student_book_bot)
            return Response(serializer.data)
        except StudentBookBot.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    ## 創建一個新的機器人ID
    def post(self, request, format=None):
        serializer = StudentBookBotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, book_id, format=None):
        try:
            student_book_bot = StudentBookBot.objects.get(student_id=user_id, book_id=book_id)
            serializer = StudentBookBotSerializer(student_book_bot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentBookBot.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

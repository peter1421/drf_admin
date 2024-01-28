import uuid
import openai
from rest_framework.response import Response
from rest_framework import status
from chatbot.models import StudentBookBot
from drf_admin.apps.courses.models import Book
from oauth.models import Users
# https://platform.openai.com/api-keys
openai.api_key = "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"  # 替换为您的 OpenAI API 密钥


def get_gpt_response(prompt):
    # 建立ChatCompletion端點的請求
    temp=''
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8NcRQDt1",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": temp+prompt},
        ],
    )
    # print(response.choices[0].message)

    return response.choices[0].message["content"]

# print(get_gpt_response("你好"))

# # 在您的視圖函數或類中
# def create_student_book_bot(request):
#     student_id = request.data.get('student_id')
#     book_id = request.data.get('book_id')
    
#     try:
#         # 獲取學生和書籍對象
#         student = Users.objects.get(id=student_id)
#         book = Book.objects.get(book_id=book_id)


#         # 創建StudentBookBot記錄
#         student_book_bot = StudentBookBot.objects.create(
#             student=student,
#             book=book,
#             bot_id=uuid.uuid4(),  # 生成新的 bot_id
#             # 其他字段的初始化
#             # ...
#         )

#         return Response({"student_book_bot_id": student_book_bot.bot_id}, status=status.HTTP_201_CREATED)
#     except Users.DoesNotExist:
#         return Response({"error": "無效的學生用戶 ID"}, status=status.HTTP_400_BAD_REQUEST)
#     except Book.DoesNotExist:
#         return Response({"error": "無效的書籍 ID"}, status=status.HTTP_400_BAD_REQUEST)
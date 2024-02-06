from django.urls import path

from chatbot.views import centre
from chatbot.views.bookbot import StudentBookBotView

# from drf_admin.apps.chatbot import views

urlpatterns = [
    ## 讓CHAYGPT回訊息跟紀錄
    ## TODO 找時間將以下api整合
    path('save-message/', centre.ChatMessageUpdateAPIView.as_view()), 
    path('get-message/', centre.GetMessageAPIView.as_view()),
    ## 書籍與機器人的關聯
    path('student-book-bot/', StudentBookBotView.as_view(), name='student-book-bot'),
    # path('student-book-bot/<int:student>/<int:book>/', StudentBookBotView.as_view(), name='student-book-bot-detail'), 
]
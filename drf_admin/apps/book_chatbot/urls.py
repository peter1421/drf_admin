from django.urls import path

from book_chatbot.views import centre
from book_chatbot.views.bookbot import StudentBookBotView


urlpatterns = [
    # path('save-message/', views.index, name='index'),
    path('save-message/', centre.ChatMessageUpdateAPIView.as_view()),
    # path('save-message/', centre.SaveMessageAPIView.as_view()),
    path('get-message/', centre.GetMessageAPIView.as_view()),
    path('student-book-bot/', StudentBookBotView.as_view(), name='student-book-bot'),
    # path('student-book-bot/<int:student>/<int:book>/', StudentBookBotView.as_view(), name='student-book-bot-detail'),
]
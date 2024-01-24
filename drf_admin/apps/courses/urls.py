from django.urls import path

from courses.views import books

# from drf_admin.apps.chatbot import views

urlpatterns = [
    path('books/', books.BooksViewSet.as_view(), name='book-list'), 
    path('books/<int:pk>/', books.BooksViewSet.as_view(), name='book-detail'),  
]
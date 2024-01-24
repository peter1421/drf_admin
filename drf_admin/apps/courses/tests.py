from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Book
from django.urls import reverse
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # 導入 get_user_model

class BooksViewSetTestCase(TestCase):
    def setUp(self):
        # 獲取當前使用的用戶模型
        User = get_user_model()
        # 創建一個測試用戶
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # 強制身份驗證
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # 創建一本測試書籍
        self.book = Book.objects.create(name="Test Book", author="Test Author")

    def test_list_books(self):
        # 測試書籍列表
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 這裡可以添加更多關於回應內容的斷言

    def test_retrieve_book(self):
        # 測試獲取單一書籍
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 這裡可以添加更多關於回應內容的斷言

    # 這裡可以添加創建、更新和刪除書籍的測試

    def tearDown(self):
        # 測試結束後清理測試數據
        pass

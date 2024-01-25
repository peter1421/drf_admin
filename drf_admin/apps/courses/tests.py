# import pytest
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from courses.models import Book

# # 將 authenticated_client 定義為一個 fixture
# @pytest.fixture
# @pytest.mark.django_db
# def authenticated_client():
#     User = get_user_model()
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     client = APIClient()
#     client.force_authenticate(user=user)
#     return client

# # 將 book_data 定義為一個 fixture
# @pytest.fixture
# def book_data():
#     return {
#         'name': 'New Book',
#         'description': 'Description',
#         'content': 'Content',
#         'author': 'New Author',
#         'publisher': 'Publisher',
#         'publish_date': '2023-01-01',
#         'category': 'fiction',
#         'difficulty': 'easy'
#     }

# # 將 existing_book 定義為一個 fixture
# @pytest.fixture
# @pytest.mark.django_db
# def existing_book():
#     return Book.objects.create(name="Test Book", author="Test Author")

# # 測試書籍列表查詢
# def test_list_books(authenticated_client):
#     url = reverse('book-list')  # 確保這是掛載 BooksViewSet 的 URL 名稱
#     response = authenticated_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Book
from django.urls import reverse
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

    def test_create_book(self):
        # 測試創建書籍
        book_data = {
            'name': 'New Book', 
            'description': 'Description', 
            'content': 'Content', 
            'author': 'New Author', 
            'publisher': 'Publisher', 
            'publish_date': '2023-01-01', 
            'category': 'fiction', 
            'difficulty': 'easy'
        }
        response = self.client.post(reverse('book-list'), book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 檢查響應數據
        if response.status_code == status.HTTP_201_CREATED:
            response_data = response.json()
            book_response_data = response_data['data']  # 獲取實際的書籍數據
            self.assertEqual(book_response_data['name'], book_data['name'])
            self.assertEqual(book_response_data['description'], book_data['description'])
            self.assertEqual(book_response_data['content'], book_data['content'])
            self.assertEqual(book_response_data['author'], book_data['author'])
            self.assertEqual(book_response_data['publisher'], book_data['publisher'])
            self.assertEqual(book_response_data['publish_date'], book_data['publish_date'])
            self.assertEqual(book_response_data['category'], book_data['category'])
            self.assertEqual(book_response_data['difficulty'], book_data['difficulty'])
        

    def test_update_book(self):
        # 測試更新書籍
        updated_data = {'name': 'Updated Book', 'author': 'Updated Author'}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), updated_data)  # 使用書籍詳情的URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 檢查響應數據

    def test_delete_book(self):
        # 測試刪除書籍
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))  # 使用書籍詳情的URL
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # 檢查書籍是否被刪除
    def tearDown(self):
        # 測試結束後清理測試數據
        pass

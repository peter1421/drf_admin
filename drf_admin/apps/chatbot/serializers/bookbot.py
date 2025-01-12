from chatbot.backend import create_chatroom
from rest_framework import serializers

from chatbot.models import StudentBookBot
from courses.serializers.books import BooksSerializer
from system.serializers.users import UsersSerializer
from drf_admin.apps.courses.models import Book
from oauth.models import Users

class StudentBookBotSerializer(serializers.ModelSerializer):
    # student = UsersSerializer(read_only=True)
    # book = BooksSerializer(read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = StudentBookBot
        fields = ['bot_id', 'student', 'book','now_chatroom_id']

    def create(self, validated_data):
        # 创建 StudentBookBot 实例
        student = UsersSerializer(read_only=True)
        book = BooksSerializer(read_only=True)
        student = validated_data.pop('student', None)
        book = validated_data.pop('book', None)
        now_chatroom_id = validated_data.pop('now_chatroom_id', None)
        if now_chatroom_id == 'first':
            now_chatroom_id = create_chatroom(book)
            student_book_bot = StudentBookBot.objects.create(student=student,book=book, now_chatroom_id=now_chatroom_id)
        else:
            student_book_bot = StudentBookBot.objects.get(student=student,book=book)
            student_book_bot.now_chatroom_id=now_chatroom_id
            student_book_bot.save()
        return student_book_bot

    def to_representation(self, instance):
        # 定制 GET 请求的输出
        representation = super(StudentBookBotSerializer, self).to_representation(instance)
        representation['student'] = UsersSerializer(instance.student).data
        representation['book'] = BooksSerializer(instance.book).data
        return representation

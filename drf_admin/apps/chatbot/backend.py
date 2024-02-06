import time
from django.conf import settings
from openai._client import OpenAI

from chatbot.models import StudentBookBot


# https://platform.openai.com/api-keys

def continue_conversation(user_input,thread_id,api_key,assistant_id):
    # 設定 API 密鑰和助理 ID
    # API_KEY = "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"
    # ASSISTANT_ID = "asst_WWGWWbt5iReBr3MlkFOh4NqG"
    API_KEY=api_key
    ASSISTANT_ID=assistant_id
    print("api_key",API_KEY)
    print("assistant_id",ASSISTANT_ID)
    client = OpenAI(api_key=API_KEY)
    # 添加用户的新消息到对话中
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input
    )

    # 創建一個新的運行
    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=ASSISTANT_ID)

    # 等待運行完成
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        time.sleep(1)

    # 獲取最新消息
    message_response = client.beta.threads.messages.list(thread_id=thread_id)
    messages = message_response.data
    latest_message = messages[0].content[0].text.value
    
    # 記錄回應
    # for message in messages:
    #     print(message.content[0].text.value)

    # print(f"💬魚姐姐: {latest_message}")
    return latest_message

def get_book_id(student_book_bot_id):
    student_book_bot = StudentBookBot.objects.get(bot_id=student_book_bot_id)
    book_id = student_book_bot.book.book_id
    return book_id

def find_api_by_id(book_id):
    # 通过书ID找到书名
    book_name = settings.BOOK_ID_TO_NAME.get(book_id)
    if not book_name:
        return "Book ID not found."

    # 通过书名找到对应的配置
    book_config = settings.BOOK_CONFIGS.get(book_name)
    if not book_config:
        return "Book config not found."
    return book_config


def get_response(user_input,thread_id,student_book_bot_id):
    book_id = get_book_id(student_book_bot_id)
    config = find_api_by_id(book_id)
    if config:
        assistant_id = config["ASSISTANT_ID"]
        api_key = config["API_KEY"]
        response = continue_conversation(user_input,thread_id,api_key,assistant_id)
        return response
    return "No response found"

def creat_chatroom(book):
    config = find_api_by_id(book.book_id)
    content=f"魚姐姐，你好! 請你問我跟「{book.name}」的問題"
    API_KEY=config["API_KEY"]
    client = OpenAI(api_key=API_KEY)
    thread = client.beta.threads.create(
        messages=[
            {"role": "user", "content":content}
        ]
    )
    print(thread.id)
    return thread.id
from django.conf import settings


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
    # 返回找到的配置信息
    # return {
    #     "ASSISTANT_ID": book_config["ASSISTANT_ID"],
    #     "API_KEY": book_config["API_KEY"]
    # }
print(settings.BOOK_ID_TO_NAME)
# 例如，要找书ID为28的API，可以调用
# api_info = find_api_by_id(28)
# print(api_info)
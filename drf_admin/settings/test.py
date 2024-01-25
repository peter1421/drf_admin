from .settings import *  # 导入所有默认设置

# 设置测试使用的数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

# 禁用影响测试的应用
INSTALLED_APPS.remove('easyaudit')

"""
Django settings for drf_admin project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os
import sys

import psutil

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mppodn1q7pk7hh)da39+yc1$^rcovyc)$lt69*wprdz_mjayaa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 解决跨域问题
    'corsheaders',
    # model过滤
    'django_filters',
    # swagger
    'drf_yasg',
    # WebSocket
    'channels',
    # django_user_agents
    'django_user_agents',
    # 定时任务
    'django_apscheduler',
    # crud变更记录
    'easyaudit',
    # 注册apps
    'oauth',
    'system',
    'monitor',
    'cmdb',
    'information',
    'book_chatbot',
    'courses',
    # 'drf_admin.apps.courses',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django_user_agents
    'django_user_agents.middleware.UserAgentMiddleware',
    # IP黑名单校验
    'drf_admin.utils.middleware.IpBlackListMiddleware',
    # 在线用户监控
    'drf_admin.utils.middleware.OnlineUsersMiddleware',
    # crud变更记录中间件
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    # 下面两个中间件放置在最后位置, 且两者保证顺序
    'drf_admin.utils.middleware.OperationLogMiddleware',
    'drf_admin.utils.middleware.ResponseMiddleware',
]

# CORS跨域设置(3.0版本后需增加http)
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:9527',
    'http://localhost:9527',
)
# 允许携带cookie
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'drf_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_admin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Redis
REDIS_PWD = os.getenv('REDIS_PWD', '')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
if REDIS_PWD:
    REDIS_STR = f':{REDIS_PWD}@'
else:
    REDIS_STR = ''
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # session
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 用户信息/ip黑名单
    'user_info': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 在线用户监测
    'online_user': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/3',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}
# 设置Django session使用redis作为后端存储
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 指定自定义的用户模型
AUTH_USER_MODEL = 'oauth.Users'

# DRF配置
REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'drf_admin.utils.exceptions.exception_handler',
    # 全局分页
    'DEFAULT_PAGINATION_CLASS': 'drf_admin.utils.pagination.GlobalPagination',
    'DEFAULT_PERMISSION_CLASSES':
        (
            'rest_framework.permissions.IsAuthenticated',  # 登录验证
            'drf_admin.utils.permissions.RbacPermission',  # 自定义权限认证
        ),
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # DRF-JWT认证
        ),
    # DRF-API文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_THROTTLE_RATES': {'anon': '10/min', }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # Token有效时间
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token刷新有效时间
    'JWT_ALLOW_REFRESH': True,  # 允许刷新Token
    # 定义Token携带头信息, Authorization: Bearer ...
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

AUTHENTICATION_BACKENDS = [
    'oauth.utils.UsernameMobileAuthBackend',  # 自定义用户认证方法
]

DEFAULT_PWD = os.getenv('DEFAULT_PWD', '123456')  # 创建用户默认密码
BASE_API = 'api/'  # 项目BASE API, 如设置时必须以/结尾
WHITE_LIST = [f'/{BASE_API}oauth/login/',
              f'/{BASE_API}oauth/info/', f'/{BASE_API}swagger/.*']  # 权限认证白名单
REGEX_URL = '^{url}$'  # 权限匹配时,严格正则url
PROJECT_START_TIME = psutil.Process().create_time()

# Swagger配置 https://github.com/axnsan12/drf-yasg/issues/58
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

# channels配置(配置ASGI, 用于实现WebSocket)
ASGI_APPLICATION = 'drf_admin.routing.application'

# django-channels配置
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels_redis.core.RedisChannelLayer",
        'CONFIG': {
            'hosts': [f'redis://{REDIS_STR}{REDIS_HOST}:{REDIS_PORT}/4'],
            'symmetric_encryption_keys': [SECRET_KEY],
            'capacity': 1500,
            'expiry': 10
        },
    },
}

# simpleui配置项
SIMPLEUI_HOME_INFO = False  # 设置admin站点不显示simpleui的git页

# django-easy-audit配置
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS = False
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = False

# 日志配置
LOGS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'standard': {
            'format': '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d]==>[%(message)s]'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s]==>[%(message)s]'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_info.log'),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 向终端中输出日志
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'operation': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_operation.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'query': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_query.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_error.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },

    },
    'loggers': {
        # 记录视图中手动info日志
        'info': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 非GET方法操作日志
        'operation': {
            'handlers': ['operation', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # GET方法查询日志
        'query': {
            'handlers': ['query', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 记录视图异常日志
        'error': {
            'handlers': ['error', 'console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

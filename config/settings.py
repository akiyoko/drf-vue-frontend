import os


###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


############
# Security #
############

SECRET_KEY = '$9dq3!ufg1w5w&*52pc!-63+tqb#3n)y*x8($=!^qj!t4f!7ml'

DEBUG = True

ALLOWED_HOSTS = []


#################
# Core settings #
#################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'rest_framework',          # 追加
    'djoser',                  # 追加
    'corsheaders',             # 追加

    # My applications
    'apiv1.apps.Apiv1Config',  # 追加
    'shop.apps.ShopConfig',    # 追加
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 追加
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


###########
# Logging #
###########

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                      '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja'      # 修正

TIME_ZONE = 'Asia/Tokyo'  # 修正

USE_I18N = True

USE_L10N = True

USE_TZ = True


################
# Static files #
################

STATIC_URL = '/static/'


##################
# REST Framework #
##################

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # 追加
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 追加
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),  # 追加
}


########
# CORS #
########

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    '127.0.0.1:8080',
)

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-kfal^v_0hd50^m4!8d3gc3ati$3=g(_^zr5_v=0-psz$nh&)@9'


DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'game',
    "crispy_forms",
    "crispy_bootstrap5"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'secret_santa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'secret_santa.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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



LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True




STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHOICES = [
    ('Новый смартфон.', 'Новый смартфон.'),
    ('2', 'Настольная игра.'),
    ('3', '5-10 килограммов мандаринов (для кого-то это настоящее счастье).'),
    ('4', 'Планшет.'),
    ('5', 'Сертификат в парк развлечений.'),
    ('6', 'Билеты в кино.'),
    ('7', 'Билеты на каток.'),
    ('8', 'Графический планшет.'),
    ('9', 'Книга.'),
    ('10', 'Сертификат на развивающий курс.'),
    ('11', 'Набор для творчества.'),
    ('12', 'Картина.'),
    ('13', 'Сертификат какого-либо магазина.'),
    ('14', 'Компьютерная игра.'),
    ('15', 'Персональный компьютер.'),
    ('16', 'Ноутбук.'),
    ('17', 'Запчасти для персонального компьютера'),
    ('18', 'Алкоголь.')
]

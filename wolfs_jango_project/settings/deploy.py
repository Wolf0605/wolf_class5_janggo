from .base import *

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secrret = secret.lstrip().rstrip()
    file.close()
    return secret
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"] #모든호스트의 접속을 허가 한다


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306', # 여기가 문제였네요 상상도 못한 정체 포트 3306입니다 5432 아니구요 ㅠ
    }
}
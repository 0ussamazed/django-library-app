from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# أسرار المشروع
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# -------------------------
# التطبيقات
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lms_app',
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

ROOT_URLCONF = 'myWebSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'myWebSite.wsgi.application'

# -------------------------
# قاعدة البيانات
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Static files
# -------------------------
STATIC_URL = '/static/'

# هذا المجلد سيجمع فيه كل ملفات static بعد collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# هنا المجلدات التي تحتوي ملفات static الأصلية (قبل جمعها)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myWebSite/static')
]

# -------------------------
# Media files
# -------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# -------------------------
# نصائح للنشر على Render
# -------------------------
# 1. قبل رفع المشروع: 
#    python manage.py collectstatic
# 2. ارفع المجلدات الناتجة:
#    - staticfiles/
#    - media/
# 3. في HTML:
#    - استخدم {% load static %} و {% static '...' %}
#    - استخدم {{ book.image.url }} للصور من media
# 4. إذا تريد رفع ملفات كبيرة على السحابة استخدم:
#    - AWS S3 أو Cloudinary للـMEDIA وSTATIC
# -------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

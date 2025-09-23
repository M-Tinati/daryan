from pathlib import Path
import os




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vbaaar50kul)_kdkmdt)p$4j&gmvw8=u&516#s9nhzg^e6ryfj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['daryan.onrender.com', 'localhost', '127.0.0.1']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
    'blog.apps.BlogConfig',
    'shop.apps.ShopConfig',
    'orders.apps.OrdersConfig',
    'pricing.apps.PricingConfig',
    "widget_tweaks",
    'django.contrib.humanize',
    'price',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',   # 👈 اول این
    'django.middleware.locale.LocaleMiddleware',   # 👈 بعد این
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'poly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'poly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'
LANGUAGE_BIDI = True  # برای RTL (fa, ar, he)

LANGUAGES = [
    ('fa', 'فارسی'),
    ('ps', 'پشتو'),
    ('ur', 'اردو'),
    ('ar', 'عربی'),
    ('ku', 'کردی'),
    ('tr', 'ترکی'),
    ('az', 'آذربایجانی'),
    ('hy', 'ارمنی'),
    ('tk', 'ترکمنی'),
    ('he', 'عبری'),
    ('en', 'English'),
    ('zh-hans', 'Chinese (Simplified)'),
    ('es', 'Spanish'),
    ('ru', 'Russian'),
    ('de', 'German'),
    ('fr', 'French'),
    ('ja', 'Japanese'),
    ('hi', 'Hindi'),
]

LOCALE_PATHS = [BASE_DIR / 'locale']  # مسیر فایل‌های .po/.mo

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    'accounts.backends.PhoneBackend',               # کاربران معمولی با phone
    'django.contrib.auth.backends.ModelBackend',    # ادمین با username
]

LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = 'accounts:login'

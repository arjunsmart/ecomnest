
import os
#from decouple import config

from pathlib import Path

#Razorpay Credentials

"""RAZORPAY_API_KEY_PUBLISHABLE = 'rzp_test_yXRx5KMNXszyBZ'
RAZORPAY_API_KEY_HIDDEN = 'M7UOx3sp90nOyppE1I0sJBo3"""

RAZORPAY_API_KEY_PUBLISHABLE = 'rzp_live_JDdaFFEnzl5E0k'
RAZORPAY_API_KEY_HIDDEN = '1tRyttAAMjU3MjtQjrv48RaM'

#Stripe Credentials

STRIPE_API_KEY_PUBLISHABLE = 'pk_test_51HExIMKDElO4WcAHfqjndMm4KvMfCTIikx1gCAaHs2sKNe9jLkAnxEKPnGpppHr093cwO9FwhsGrxnk4nFhiXUJj00gHy36hXk'
STRIPE_API_KEY_HIDDEN = 'sk_test_51HExIMKDElO4WcAHQz4emdMtWFygfDJxq73kL0clriKKj650kl1s2UNwXnlPg7dAwvyIfMCaGPFb4MTVt97VumYC009JAUDZZ9'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w(usn!n0dl=p5uhdwgo=n2d9@pb+)y0k63)2v9h447x7m)dw1f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'cart'
LOGOUT_REDIRECT_URL = 'frontpage'

# Cart

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'apps.cart',
    'apps.coupon',
    'apps.core',
    'apps.newsletter',
    'apps.order',
    'apps.store',
    'apps.userprofile'
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

ROOT_URLCONF = 'farmersnest.urls'

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
                'apps.store.context_processors.menu_categories',
                'apps.coupon.context_processors.menu_coupons',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'farmersnest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/ubuntu/farmer_nest/auth/mysql.conf',
            },
    }
}'''


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'root')

'''MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')'''
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#smtp configurations

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT =587
EMAIL_USE_TLS =True
EMAIL_HOST_USER ='knagaraju1980@gmail.com'
EMAIL_HOST_PASSWORD = ''
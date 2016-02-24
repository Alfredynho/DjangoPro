from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'omt6nbk#)yvgry-%z0u)@1@61#c*l2z29!1j9x#%ajb#u^0_9d'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	)

#Aplicaciones de terceros
THIRD_PARTY_APPS = (

	)

#aplicaciones locales
LOCAL_APPS = (

	)


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/La_Paz'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
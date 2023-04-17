from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB','p_db'),
        'USER': os.environ.get('POSTGRES_USER','postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD','postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
    }
}
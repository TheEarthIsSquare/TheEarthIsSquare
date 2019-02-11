from theearthissquare.settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

SECURE_SSL_REDIRECT = True

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']

AWS_S3_REGION_NAME = 'ap-southeast-2'

AWS_S3_ENDPOINT_URL = 'https://s3-ap-southeast-2.amazonaws.com'

S3DIRECT_DESTINATIONS = {
    'profiles': {
        'key': 'uploads/profiles',
    },
    'projects': {
        'key': 'uploads/projects'
    }
}

# Inherit from standard settings file for default
from theearthissquare.settings import *

# Everything below will override our standard settings:
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Set debug to False
DEBUG = False

SECURE_SSL_REDIRECT = True

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']

AWS_S3_REGION_NAME = 'ap-southeast-2'

AWS_S3_ENDPOINT_URL = 'https://ap-southeast-2.amazonaws.com'

S3DIRECT_ENDPOINT = 's3.amazonaws.com'  # http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_DIR = 's3direct'  # (optional, default is 's3direct', location within the bucket to upload files)
S3DIRECT_UNIQUE_RENAME = False # (optional, default is 'False', gives the uploaded file a unique filename)

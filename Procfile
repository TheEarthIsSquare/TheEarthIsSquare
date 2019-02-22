release: python manage.py migrate
worker: celery -A theearthissquare worker -l info -B
web: waitress-serve --port=$PORT theearthissquare.wsgi:application

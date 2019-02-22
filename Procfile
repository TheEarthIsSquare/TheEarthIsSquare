release: python manage.py migrate
worker: celery worker --app=tasks.app
web: waitress-serve --port=$PORT theearthissquare.wsgi:application

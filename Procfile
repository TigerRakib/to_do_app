web: gunicorn to_do_app.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn to_do_app.wsgi
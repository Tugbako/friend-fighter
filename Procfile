release: python manage.py migrate --no-input
release: python manage.py collectstatic --noinput
web: gunicorn friend_fighter.wsgi --log-file -

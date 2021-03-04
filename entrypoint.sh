##!/bin/sh
#
##sleep 10
##
##python manage.py migrate
##python manage.py createcachetable
##python manage.py collectstatic  --noinput
##gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
##
##exec "$@"
#
#sleep 2
#python manage.py migrate
#python manage.py createcachetable
#
#if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
#  python manage.py createsuperuser \
#    --noinput \
#    --username "$DJANGO_SUPERUSER_USERNAME" \
#    --email $DJANGO_SUPERUSER_EMAIL
#fi
#
#python manage.py collectstatic --noinput
#gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
#
#exec "$@"
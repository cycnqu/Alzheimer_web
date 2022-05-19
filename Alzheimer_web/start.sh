#!/bin/bash
python manage.py collectstatic --noinput&&
uwsgi --log-master --ini /var/www/html/Alzheimer_web/uwsgi.ini&&
tail -f /dev/null

exec "$@"

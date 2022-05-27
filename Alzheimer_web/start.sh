#!/bin/bash
python manage.py collectstatic --noinput&&
uwsgi --ini /var/www/html/myproject/uwsgi.ini&&
tail -f /dev/null

exec "$@"

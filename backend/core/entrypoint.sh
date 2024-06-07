#!/bin/bash
echo "Collect static files"
python manage.py collectstatic --noinput
chmod 777 /home/app/web/static/

echo "Apply database migrations"
until python manage.py migrate
do
  echo "Waiting for db to be ready..."
  sleep 2
done

exec "$@"
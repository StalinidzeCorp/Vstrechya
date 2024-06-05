#!/bin/bash
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
until python manage.py migrate
do
  echo "Waiting for db to be ready..."
  sleep 2
done

# --> Duplicate logs to stdout for portainer console
echo "--> Starting prod logs"
tail -f /logs/gunicorn/access.log > /dev/stdout &
tail -f /logs/gunicorn/error.log > /dev/stderr &

exec "$@"
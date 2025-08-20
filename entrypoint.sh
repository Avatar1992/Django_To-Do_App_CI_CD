#!/bin/sh

# Exit immediately if a command exits with non-zero
set -e

echo "📦 Running migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# (Optional) Auto-create a superuser if none exists
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    echo "👤 Creating superuser..."
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL || true
fi

echo "🚀 Starting Django server..."
exec "$@"


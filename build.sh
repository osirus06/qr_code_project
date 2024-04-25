#!/usr/bin/env bash


set -o errexit  # exit on error

echo "Starting build script..."

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Run Django migrations
echo "Running migrations..."
python manage.py migrate
echo "Build script completed."




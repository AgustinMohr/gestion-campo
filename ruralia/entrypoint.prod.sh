#!/bin/bash

echo "Esperando a que Postgres esté listo..."

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done

echo "Postgres disponible. Ejecutando migraciones..."

python manage.py migrate
python manage.py runserver 0.0.0.0:8000

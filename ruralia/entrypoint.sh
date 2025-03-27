#!/bin/sh

if [ "$DATABASE_NAME" = "ruralisdb" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate

python manage.py loaddata users

python create_superuser.py

python manage.py runserver 0.0.0.0:8000


# python manage.py shell "from usuarios.models import Usuario; Usuario.objects.create_superuser('admin', 'admin@example.com', 'admin')"
# python manage.py flush --no-input


exec "$@"
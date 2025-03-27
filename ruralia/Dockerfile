# Use the official Python runtime image

FROM python:3.13

RUN apt-get update && apt-get install -y postgresql-client netcat-openbsd

RUN useradd -m myuser
USER myuser
WORKDIR /myuser

RUN mkdir /myuser/app

#Cambia el propietario del directorio a myuser para asegurar permisos correctos.
RUN chown -R myuser:myuser /myuser/app

WORKDIR /myuser/app

RUN pip install --upgrade pip


# Set environment variables 

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# # Copy the Django project  and install dependencies
# COPY ./requirements.txt  ./
 
# # run this command to install all dependencies 
# RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container
# COPY ./ ./


COPY --chown=myuser:myuser ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

RUN pip install djangorestframework-jsonapi['django-filter']

ENV PATH="/myuser/.local/bin:${PATH}"

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /myuser/app/entrypoint.sh
RUN chmod +x /myuser/app/entrypoint.sh

# copy project
COPY --chown=myuser:myuser . .

# RUN python /myuser/app/create_superuser.py

# run entrypoint.sh
ENTRYPOINT ["/myuser/app/entrypoint.sh"]



# Expose the Django port
# EXPOSE 8000
 
# Run Django’s development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] <- SE EJECUTA EN docker-compose.yml
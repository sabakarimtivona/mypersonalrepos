# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8

COPY . code
WORKDIR /code
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY env.sh .
RUN chmod +x /code/env.sh
RUN /bin/bash -c "./env.sh"

# Mounts the application code to the image


EXPOSE 80

# CMD ["python3" , "manage.py", "collectstatic"]
# CMD ["python3","manage.py", "makemigrations"]
# CMD ["python3", "manage.py", "migrate"]
CMD ["gunicorn", "pricing_data.wsgi:application", "--config", "gunicorn.conf.py"]
# ENTRYPOINT ["python", "manage.py"]
# CMD ["collectstatic","makemigrations","migrate"]


FROM python:3.10-slim-buster

# Path: /app
WORKDIR /app
# Copy local code to the container image.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
# Run the web service on container startup.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

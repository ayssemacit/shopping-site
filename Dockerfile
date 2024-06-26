FROM python:3.11.2


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENV DJANGO_SETTINGS_MODULE=ecommerce.settings


EXPOSE 8080


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /app/
EXPOSE 8005
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]

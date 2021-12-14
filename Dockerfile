FROM python:3.10

WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# Now copy in our code, and run it
COPY . /code
EXPOSE 8005
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
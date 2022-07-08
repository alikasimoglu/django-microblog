# django-microblog

This is a test microblog project created using Django 4.0. But don't worry this is a fully working project. There is no super-amazing front-end, just back-end codes with minimal html :)

```bash
$ git@github.com:alikasimoglu/django-microblog.git
$ docker-compose up
```
Now you can access the application at <https://localhost:8005//blogs> and the admin site
at <https://localhost:8005/admin>.

Stack and version numbers used:

| Name           | Version  |
|----------------|----------|
| Django         | 4.0.6      |
| Python         | 3.10     |


## Folder structure
```
.
├── blogs                   # blog app
├── nikidaemTestProject     # main project files needed for configuration
├── profiles                # profiles app
├── templates               # main templates
├── .env-example            # environments file
├── .gitignore              # files exluded from github
├── db.sqlite3              # database
├── docker-compose.yaml     # docker-compose setup with container orchestration instructions
├── Dockerfile              # general Dockerfile of the main server
├── manage.py
├── README.md               # this file
└── requirement.txt         # python requirements
```

Project using only SQLite database because of it's a test project. But easily can be changed to PostgreSQL. 

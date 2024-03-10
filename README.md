# Team Management Project Setup on Server (Ubuntu)

## Install Python 3.12.2

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12.2
```

## Install Python 3.12-venv

```bash
sudo apt install python3.12-venv
```

## Create Virtual Environment

```bash
cd team_management
python3.12 -m venv venv
```

## Activate Virtual Environment

```bash
source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt --cache-dir .pip_cache
```

## Install gettext for translations

```bash
sudo apt-get install gettext
```

## Create Application File

This is to help you configure a new app. You can skip this step if you are configuring an existing app.

Create new env file for the app.

> <app_name> is the name of the app you want to configure. For example, if you want to configure the `team_management` app, then the command will be `cp .env.example .env.team_management`

```bash
cd src/config/apps
cp .env.example .env.<app_name>
```

Create new python file for the app.

```bash
cd src/config/apps
cp example.py <app_name>.py
```

Edit the new python file and change the `example` to the name of the app.

Edit STYLE dictionary configuration in the new python file to the values you want.

Then edit the env files and add the correct values.

## Run Migrations

```bash
DJANGO_SETTINGS_MODULE=config.apps.<app_name> python manage.py migrate
```

For example, there is already a default app called `example`. So, if you want to run the migrations for the `example` app, then the command will be `DJANGO_SETTINGS_MODULE=config.apps.example python manage.py migrate`

## Compile django.po translation files

```bash
DJANGO_SETTINGS_MODULE=config.apps.<app_name> python manage.py compilemessages -l
```

For example, there is already a default app called `example`. So, if you want to compile the translations for the `example` app, then the command will be `DJANGO_SETTINGS_MODULE=config.apps.example python manage.py compilemessages -l`

## Create Superuser

```bash
DJANGO_SETTINGS_MODULE=config.apps.<app_name> python manage.py createsuperuser
```

For example, there is already a default app called `example`. So, if you want to create a superuser for the `example` app, then the command will be `DJANGO_SETTINGS_MODULE=config.apps.example python manage.py createsuperuser`

## Run Server

```bash
DJANGO_SETTINGS_MODULE=config.apps.<app_name> python manage.py <command>
```

For example, there is already a default app called `example`. So, if you want to run the server for the `example` app, then the command will be `DJANGO_SETTINGS_MODULE=config.apps.example python manage.py <command>`

Always ensure the `DJANGO_SETTINGS_MODULE` is set before running any command. Even gunicorn (application server) needs this environment variable to be set.

## Notes

1. App name must not contain any spaces or special characters. It must be a valid python module name.


## Environment Variables

This is an explanation of the environment variables used in the `.env.example` file.

### SECRET_KEY

This is the secret key used by Django to encrypt and decrypt data. It is used to sign cookies and other sensitive data. It is also used to generate CSRF tokens. It is important that this key is kept secret. It should not be shared with anyone. It should not be committed to version control. It should not be stored in a database. It should not be stored in a file. It should only be stored in an environment variable.

### DEBUG

This is a boolean value that determines whether the app is in debug mode or not. It should be set to `True` when developing the app. It should be set to `False` when deploying the app to production.



> All the database files can be found in `src/config/dbs` directory.
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
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Server

```bash
python manage.py runserver
```

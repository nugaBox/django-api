# Django API Sample


### Python 가상환경 및 라이브러리 설치

```bash
python3 -m venv ./venv
source venv/bin/activate
(venv) pip3 install -r requirements.txt
```

### Django 프로젝트 시작

```bash
django-admin startproject app
cd app
python3 manage.py startapp api
```

### Django 마이그레이션

```bash
python3 manage.py makemigrations api
python3 manage.py migrate
```

### Django 서버 시작

```bash
python3 manage.py runserver
```

### API Document 접속
- Swagger : http://127.0.0.1:8000/docs
- Redoc :  http://127.0.0.1:8000/redoc

## install

### requirements
- python 3.7+
- pip
- poetry

```shell script
pip install poetry
poetry install --no-dev
poetry run python manage.py migrate
```

## launch

```shell script
poetry run python manage.py runserver
```

## access

**браузер апи (частично)**: http://localhost:8080/api/  
**веб-версия для сотрудников для пк**: http://localhost:8080/  
**административная панель (расширенная версия для пк)**: http://localhost:8080/admin/

# Cookiecutter Flask API

API (backend python) for the flask_cookie-clone frontend. Built with [Cookiecutter flask OpenAPI](https://github.com/huogerac/cookiecutter-flask-openapi/
)

## Setup

Install dependencies:

```bash
$ pip install -r requirements-dev.txt
```

Run tests:

```bash
$ make run_tests
```

Or:

```bash
$ make db_test_up
$ pytest
$ make db_test_down
```

Run the API:

```bash
$ docker-compose up -d
$ flask db upgrade     # 1a vez apenas
$ flask run
```

👉 http://localhost:5000/api/
👉 http://localhost:5000/api/news

## Next steps

- https://github.com/confraria-devpro/flask_cookie-api/issues

## Adding a news item example

```
flask shell

Python 3.9.5 (...)

from flask_cookie.ext.database import db
from flask_cookie.models.news import News
from flask_cookie.models.users import User

News.query.all()
[]


u = User(name="roger", username="rac", email="r@a.c")
db.session.add(u)
db.session.commit()

n = News(title="Teste", description="1o. teste", author_id=u.id)
db.session.add(n)
db.session.commit()

News.query.all()
[Teste]
```

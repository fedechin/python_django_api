# python_django_api
a basic django rest-framework api done in a live coding enterview

# usage
first create a virtual enviroment and activate it

```shell script
python3 -m venv env
```
```shell script
source env/bin/activate
```

install the requirements
```shell script
pip install - r requirements.txt
```

navigate to the project folder
```shell script
cd core
```

Load seed jokes data
```shell script
python manage.py loaddata seed/*
```

# Swagger Docs
swagger Docs can be found in
http://localhost:8000/swagger/
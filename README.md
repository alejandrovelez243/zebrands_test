# Test for backend role
This is the project for the test to zebrands company

## Setup

Before start secure you have installed a local db on postgres or just one configured for all the team

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/alejandrovelez243/zebrands_test.git
$ cd zebrands_test
```

Create a virtual environment to install dependencies in and activate it:

## Linux
```sh
$ virtualenv .env
$ source env/bin/activate
```
## Windows

```bash
$ virtualenv .env
$ .\.env\Scripts\activate
```


Then install the dependencies:

```sh
(.env)$ pip install -r requirements.dev.txt
```

Then go to the setting.py file and change the databse credentials for your own
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_name",
        "USER": "username",
        "PASSWORD": "password",
        "HOST": "hostname",
        "PORT": "5432",
    }
}
```

Once `pip` has finished downloading the dependencies and you have configured your database credentials:
```sh
(.env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.

When you see that the project run succesfully, run the next command to create a superuser, so you can get to the admin portal
```sh
(.env)$ python manage.py createsuperuser
```
## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(.env)$ python manage.py test
```

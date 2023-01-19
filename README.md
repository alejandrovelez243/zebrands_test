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

Create a postgres db in your local env with the following values:
```sh
username=postgres
password=123
host=localhost
port=5432
db_name=zebrands
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

## Heroku page
You can get access to the deplyed app in heroku on this page https://zebrands.herokuapp.com/

and can go to https://zebrands.herokuapp.com/api and get the apis


# API Documentation

## Token
This apis response with a valid token for the user that is on the body with the password
```sh
curl --location --request POST 'https://zebrands.herokuapp.com/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "username",
    "password": "password"
}'
```
as test proposes, you can use the username=admin, and password=abc1234*

## Products apis
These apis contains all related to the product.
### list
Returns the list of all products even if the user is not authenticated
```sh
curl --location --request GET 'https://zebrands.herokuapp.com/api/products/' \
--header 'Authorization: Token {Valid token}'
```
In this case you can see the token in the header, but is just to show you how can we authenticate
the user, due it is not required.
### Create
```sh
curl --location --request POST 'https://zebrands.herokuapp.com/api/products/' \
--header 'Authorization: Token {Valid token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sku": "123",
    "name": "Sales force 1",
    "brand": "nike"
}'
```
### Update
```sh
curl --location --request PUT 'https://zebrands.herokuapp.com/api/products/{id}/' \
--header 'Authorization: Token {Valid token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id": 1,
    "sku": "123",
    "name": "Sales force 1",
    "brand": "nike"
}'
```
### Delete
```sh
curl --location --request DELETE 'https://zebrands.herokuapp.com/api/products/{id}/' \
--header 'Authorization: Token {Valid token}'
```

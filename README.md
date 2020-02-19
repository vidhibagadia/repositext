# Repositext

Content management server written with Python/Django.

## How to setup for development

* Install Python 3.8.1 -- Using (pyenv)[https://github.com/pyenv/pyenv] is highly recommended.
* Clone this repo to a folder.

```
# git clone git@github.com:hseritt/repositext.git
```

* Change to the project directory (repositext).
* Install the packages in requirements.txt:

```
# pip install -r requirements.txt
```

Be aware that you can use any database you like (even SQLite3 if you don't have a db server configured) but the project is set up to use MySQL.

* Run the project:

```
# ./manage.py runserver
```

You'll likely see a warning message saying that models may need to be migrated. You can do that like so:

```
# ./manage.py makemigrations
# ./manage.py migrate
```

After starting the development server, you can access http://localhost:8000 or http://localhost:8000/admin if desired.

In order to use the admin console, you'll need to set up a superuser like so:

```
# ./manage.py createsuperuser
```

Follow the directions and you should then have a superuser login with password.

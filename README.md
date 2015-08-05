# Floodinfo-Myanmar

### Setup Instructions

Clone the repo. Provided that you have `python` and `virtualenv`, `virtualenvwrapper` installed.

Firstly, create a virtual environment for the project.
```
mkvirtualenv floodinfo-env
```

Install required packages.
```
pip install -r requirements.txt
```

If you haven't installed `postgres`, install it in your system. On Mac, you could use [postgresapp](http://postgresapp.com/) from Heroku or install it from a package manager _(that's cool, too)_. Create a local db named `floodinfo`.
```
createdb floodinfo
```

Sync the database schema and migrations.
```
./manage.py migrate
```

Run the development server
```
./manage.py runserver
```

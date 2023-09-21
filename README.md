# jiu-jitsu-notes-api

The Django API for my Jiu Jitsu notes app - designed to simplify the process of conceptualising and memorising complex techniques and transitions in the sport of Jiu Jitsu.

## Setup

Clone and enter the repository

```
$ git clone https://github.com/matt-plank/jiu-jitsu-notes-api.git
$ cd jiu-jitsu-notes-api
```

Install dependencies

```
$ python -m pip install -r requirements.txt
```

Install pre-commit hooks

```
$ pre-commit install
```

### Start the Server

```
$ cd JiuJitsuNotes/
$ python manage.py runserver
```

### Run Unit Tests

```
$ cd JiuJitsuNotes/
$ python manage.py test
```

See something similar to

```
Found 20 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....................
----------------------------------------------------------------------
Ran 20 tests in 0.137s

OK
Destroying test database for alias 'default'...
```

### Create a Super User

Useful for admin dashboard access

```
$ cd JiuJitsuNotes/
$ python manage.py createsuperuser
```

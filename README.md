# SiteSwap

Discover the best sites on the internet

## Getting Started

To set up and run the project on your local machine, please follow these steps:

### Prerequisites

- Python 3.x (with pip)
- Git

### Installation

1. Clone the repository to your local machine:

```bash
$ git clone git@github.com:henacodes/site-swap.git

```

2. Create and activate a virtual environment
   Using venv (built-in)

```bash
$ python3 -m venv env
$ source env/bin/activate

```

3. Install project dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

Create a file db.sqlite3 and run the database migrations to create the necessary tables:

```bash
$ python manage.py makemigrations
$ python manage.py migrate

```

### Create a Superuser (optional)

If you want to access the Django admin interface, you can create a superuser account:

```bash
$ python manage.py createsuperuser
```

### Run the Development Server

Start the development server to run the Django project locally:

```
python manage.py runserver

```

### Contribution

If you would like to contribute to the project, fork the repo, initialize a new branch and create a PR

python --version
pip install virtualenv
mkdir django_project
cd django_project
python -m venv venv
venv/Scripts/activate


pip install django
python -m pip install django
django-admin --version


django-admin startproject core .
python manage.py runserver


# to create migration file
python manage.py makemigrations

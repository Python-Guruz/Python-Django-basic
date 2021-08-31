pip install django

django-admin startproject config .

python manage.py runserver

CRUD
create 
read - 1 -> Getting data from the database. It is json serializable.
update
delete

python manage.py startapp dog

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

We are going now to create our serializers so that we can make our data json serializable

pip install django-rest-framework

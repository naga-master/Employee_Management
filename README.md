# Employee_Management
Django API for Employee Management

### Start Project
Note: Project can be contained main apps , so instead of creating app,  first we create a project and create a app then link the app to project

follow steps to start a project and run
```
django-admin.py startproject api

cd api

django-admin.py startapp employees
```
Change the databases engine according your need in the **DATABASES** of `api/settings.py` file.
create the database 
```
python manage.py migrate
```
create user for admin page
```
python manage.py createsuperuser --email <youremailid>  --username <username>
then app asking for set password  give the password you want and click enter
```
### Linking app to project
  now employees folder might created into the api dirtectory.
  open `api/settings.py` file add 'employees' in **INSTALLED_APPS**
  if you created a URL in the app we should link the urls in the **urlpatterns** of `api/urls.py` file
 
 
### Run Migration
once code added in the app folder(employees) should run migrations
```
python manage.py makemigrations

python manage.py migrate
```

### Run Project

```
python manage.py runserver
```

# django_project
3 basic projects of django
# django_project

Basic Django applications

# How to Install Django on Windows: Step by Step Guide
link: https://www.stanleyulili.com/django/how-to-install-django-on-windows/#install-django-on-windows

Step 1 - Open Powershell

Step 2 - Verify Python Installation
      Type python -V on the prompt to verify that Python has been successfully installed
      
        > python -V
        
Step 3 - Upgrade PipPermalink
Python now comes with pip by default. But most of the time, it comes with an old version. it is always a good practice to upgrade pip to the latest version

       > python -m pip install --upgrade pip
       
Step 4 - Create a Project DirectoryPermalink
let’s create a project directory. We will name it django_project since this tutorial is just a demo but in the real world, the project directory’s name would be forum, blog, etc.

To create the directory:

      > mkdir django_project

Change into the django_project directory:

      > cd django_project

# To create a Django app
      python manage.py startapp PROJECT_NAME

# to run the project on the server
      python manage.py runserver
      
# err :- no such table: djnago session
by default, sessions are stored in atable in django
       
       python manage.py migrate
this creats default tables 

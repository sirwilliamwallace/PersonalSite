# Personal Site Powered by [django framework](https://djangoproject.com)
## This project was built to be my personal website, But I have decided to publish it on GitHub 
# Instructions
## If you decide to give it a try
### In order to get the website working on http://127.0.0.1:8000 OR http://localhost:8000
### Create a file named 'settings_creds.json' containing the following settings
```
{
  "secrets" : {
    "SECRET_KEY": "SECRET_KEY",
    "EMAIL_HOST": "smtp.HOST.com",
    "EMAIL_PORT": SMTP PORT,
    "EMAIL_HOST_USER": "EMAIL ADDRESS of Host",
    "EMAIL_HOST_PASSWORD": "PASSWORD for Email"
  }
}
```
## Make a virtual environment and install the required libraries from requirements.txt
```
$ python3 -m venv venv
$ source venv/bin/activate
$ (venv) pip3 install -r requirements.txt
```
## Make migrations and createsuperuser  
``` 
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
```
## Run the server 
```
$ python3 manage.py runserver
```
# You should complete info In the admin panel
# TODO: 
- [ ] Comments section
- [ ] Complete README
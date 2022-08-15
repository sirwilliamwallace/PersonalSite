# Personal Site Powered by _[django framework](https://djangoproject.com)_
## This project was built to be my personal website, However I have decided to publish it on GitHub 
# _Instructions_
## _If you decide to give it a try_
### In order to get the website working on [127.0.0.1 Port 8000](http://127.0.0.1:8000) OR [localhost Port 8000](http://localhost:8000)
### Create a file named _'settings_creds.json'_ containing the following settings
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
## Make a _virtual environment_ and install the required libraries from _requirements.txt_
```
$ python3 -m venv venv
$ source venv/bin/activate
$ (venv) pip3 install -r requirements.txt
```
## Make _migrations_ and _createsuperuser_  
``` 
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
```
## Run the server 
```
$ python3 manage.py runserver
```
# You should complete the admin panel's information in order for thw website to function
# <hr />
# TODO: 
- [ ] Comments section
- [ ] Complete Search section in articles
- [ ] Complete README

<br /><br /><br /><br /><br /><br />

# Built with [Django App Generator](https://app-generator.dev/tools/django-generator/)

Starter generated with [Django Generator](https://app-generator.dev/tools/django-generator/) (an open-source service) using **Gradient Design**, best practices and up-to-date Dependencies.
In order to use the sources, follow the build instructions as presented in `Start with Docker` and `Manual Build` sections. 

- Get [Support](https://app-generator.dev/ticket/create/?generated_repo=https://github.com/app-generator/django-gradient-1754408262) via `eMail` and `Discord`
- Resources:
  - [Getting Started with Django](https://app-generator.dev/docs/technologies/django/index.html)
  - [Onboarding Kit for Developers](https://app-generator.dev/onboarding-kit/) - Premium resources for coding services in no-time.
  - [Discounts for Developers](https://app-generator.dev/discounts) - Build your own dev bundle and start fast 
  - [Build Dynamic Services with Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)
  
<br />

## Features: 

- `Up-to-date Dependencies`, Best practices
- Desing: Gradient
- Extended User Profile 
- (optional) API Generator
- (optional) Celery
- (optional) OAuth Github, Google
- (optional) CI/CD for Render
- (optional) Docker

<br />

## [Deploy on Render](https://app-generator.dev/docs/deployment/render/index.html) (free plan)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

<br /> 

## [Start Project with Docker](https://app-generator.dev/docs/technologies/docker/index.html)

> In case the starter was built with Docker support, here is the start up CMD:

```bash
$ docker-compose up --build
```

Once the above command is finished, the new app is started on `http://localhost:5085`

<br />

## Manual Build 

> Download/Clone the sources  

```bash
$ git clone https://github.com/django-gradient-1754408262.git
$ cd django-gradient-1754408262
```

<br />

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> `Set Up Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> `Start the App`

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

> `Run celery`

```bash
$ celery -A core worker --concurrency 2 -l info
```

> `Execute celery tasks`

```bash
$ python manage.py shell

# Shell commands
>> from home.tasks import add
>> result = add.delay(5, 6)
>> result.get()
11  # output
```

<br />


> `Configure GitHub Auth`

- Update `.env` wuth the GitHub Secrets 
  - `GITHUB_CLIENT_ID`
  - `GITHUB_SECRET_KEY`
- Update SignIN page

```html
{% load static socialaccount %}
{% get_providers as socialaccount_providers %}

<!-- SOCIAL Login Button-->
<form class="mb-3" action="{% provider_login_url 'github' %}" method="post" >
    {% csrf_token %}
    
    <button type="submit" class="btn btn-outline-primary" href="#">
        <i class="fab fa-github mr-0"></i>
        Login with github
    </button>
</form>
```

<br />


---
Starter built with [Django App Generator](https://app-generator.dev/tools/django-generator/) - Open-source service for developers and companies.

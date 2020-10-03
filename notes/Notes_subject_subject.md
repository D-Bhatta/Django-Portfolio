# Django-Portfolio

Notes and code about Django-Portfolio

## Table of Contents

- [Django-Portfolio](#django-portfolio)
  - [Table of Contents](#table-of-contents)
  - [Sections](#sections)
  - [Structure](#structure)
  - [About the project](#about-the-project)
  - [Getting started](#getting-started)
    - [Create the project](#create-the-project)
  - [Create a Django app](#create-a-django-app)
    - [Create the files](#create-the-files)
    - [Install the app](#install-the-app)
    - [Create a View](#create-a-view)
    - [Create a HTML template](#create-a-html-template)
    - [Register URLs](#register-urls)
  - [Add a base template](#add-a-base-template)
  - [Add styling to app](#add-styling-to-app)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
    - [Links](#links)
  - [Notes template](#notes-template)

## Sections

.

## Structure

- A Django website consists of a single project that is split into separate apps.
- The idea is that each app handles a self-contained function that the site needs to perform.
- As an example, imagine an application like Instagram
  - User management: Login, logout, register, and so on
  - The image feed: Uploading, editing, and displaying images
  - Private messaging: Private messages between users and notifications
- These are each separate pieces of functionality, so if this were a Django site, then each piece of functionality should be a different Django app inside a single Django project.
- The Django project holds some configurations that apply to the project as a whole, such as project settings, URLs, shared templates and static files.
- Each application can have its own database and has its own functions to control how the data is displayed to the user in HTML templates. The apps simply manipulate the templates, thus providing functionality.
- Each application also has its own URLs as well as its own HTML templates and static files, such as JavaScript and CSS.
- Django apps are structured so that there is a separation of logic. It supports the **Model-View-Controller** Pattern, which is the architecture on which most web frameworks are built.
- The basic principle is that in each application there are three separate files that handle the three main pieces of logic separately
  - Model defines the data structure. This is usually a database and is the base layer to an application.
  - View displays some or all of the data to the user with HTML and CSS.
  - Controller handles how the database and the view interact.
- In Django, the architecture is slightly different. Although based upon the MVC pattern, Django handles the controller part itself. There’s no need to define how the database and views interact.
- The pattern Django utilizes is called the Model-View-Template (MVT) pattern. The view and template in the MVT pattern make up the view in the MVC pattern. All you need to do is add some URL configurations to map the views to, and Django handles the rest.
- The URL configurations each return a resource or an action, which utilise the templates and views.

## About the project

- **A fully functioning blog**: In this application, you will be able to create, update, and delete blog posts. Posts will have categories that can be used to sort them.
- **A portfolio of your work**: Showcase previous web development projects here. Build a gallery style page with clickable links to projects that are completed.

## Getting started

- Install django into a virtual environment

### Create the project

- CD into `portfolio` folder
- Create a new project with `django-admin startproject personal_portfolio`
- This will create a new directory `personal_portfolio`. If you `cd` into this new directory you’ll see another directory called `personal_portfolio` and a file called `manage.py`.
- Your directory structure should look something like this

```txt
rp-portfolio/
│
├── personal_portfolio/
│   ├── personal_portfolio/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
└── venv/
```

- Reorder this slightly by moving all the files up a directory
- You should end up with something like this

```txt
rp-portfolio/
│
├── personal_portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
└── manage.py
```

- Once your file structure is set up, you can now start the server and check that your set up was successful.
- In the console, run the command `python manage.py runserver`
- Then, in your browser go to `localhost:8000`, and you should see the django welcome page.

## Create a Django app

- Create a hello world app to get started.

### Create the files

- In the console, run the command `python manage.py startapp hello_world`
- This will create another directory called hello_world with several files
  - `__init__`.py tells Python to treat the directory as a Python package.
  - `admin.py` contains settings for the Django admin pages.
  - `apps.py` contains settings for the application configuration.
  - `models.py` contains a series of classes that Django’s ORM converts to database tables.
  - `tests.py` contains test classes.
  - `views.py` contains functions and classes that handle what data is displayed in the HTML templates.

### Install the app

- In `rp-portfolio/settings.py`, add the following line of code under `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "hello_world",  # Add this line
]
```

- The project now knows that the app you just created exists. Now, we create a view to display something to a user.

### Create a View

- Views in Django are a collection of functions or classes inside the views.py file in your app directory.
- Each function or class handles the logic that gets processed each time a different URL is visited.
- A view is what handles the request send to the server. It returns a template as a render object, or handles some other functionality.
- Navigate to the `views.py` file in the `hello_world` directory.
- There’s already a line of code in there that imports `render()`.
- Add the following code

```python
from django.shortcuts import render

# Add these lines
def hello_world(request):
    return render(request, "hello_world.html", {})
```

- This defined a view function called `hello_world()`.
- When this function is called, it will render an HTML file called `hello_world.html`.
- The view function takes one argument, `request`.
- This object is an `HttpRequestObject` that is created whenever a page is loaded.
- It contains information about the `request`, such as the method, which can take several values including `GET` and `POST`.
- We now need to create the HTML template to display to the user.
- `render()` looks for HTML templates inside a directory called `templates` inside the app's directory(App being `hello_world` here).
- This function will handle views and templates to display to the user.

### Create a HTML template

- Create that directory and subsequently a file named `hello_world.html` inside it

```cmd
mkdir hello_world/templates/
echo. >> hello_world/templates/hello_world.html
```

- Add `<h1>Hello, World!</h1>` to the `hello_world.html` file

### Register URLs

- The final step is to hook up URLs so that users can visit the page.
- The project has a module called `urls.py` in which we need to include a URL configuration for the `hello_world` app.
- Inside `personal_portfolio/urls.py`, add

```python
from django.contrib import admin
from django.urls import path, include  # Add this line

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hello_world.urls")),  # Add this line
]
```

- This looks for a module called `urls.py` inside the `hello_world` application and **registers any URLs defined there**.
- Whenever there is a visitto  the root path of the server's URL (localhost:8000), the `hello_world` application’s URLs will be registered.
- Create the `hello_world.urls` module as `hello_world/urls.py`
- Inside this module, we need to import the `path` object as well as our app’s `views` module.
- Then we want to create a list of URL patterns that correspond to the various view functions.
- At the moment, we have only created one view function, so we need only create one URL.

```python
from django.urls import path
from hello_world import views

urlpatterns = [path("", views.hello_world, name="hello_world")]
```

- Restart the server and visit localhost:8000 to see the HTML template just created.
- We have created our first Django app and hooked it up to our project.

## Add a base template

We will create a base template to add to each app of the project.

- In the console, run the command `mkdir personal_portfolio/templates/`
- Create the file `personal_portfolio/templates/base.html`

We create this additional `templates` directory to store HTML templates that will be used in every Django app in the project. Each Django project can consist of multiple apps that handle separated logic, and each app contains its own templates directory to store HTML templates related to the application.

This application structure works well for the back end logic, but we want our entire site to look consistent on the front end. Instead of having to import Bootstrap styles into every app, we can create a template or set of templates that are shared by all the apps. As long as Django knows to look for templates in this new, shared directory it can save a lot of repeated styles.

Whenever we want to create templates or import scripts that are intended to be used in all Django apps inside a project, we can add them to this project-level directory and extend them inside our app templates.

- Inside `personal_portfolio/templates/base.html` add the following

```html
{% block page_content %}{% endblock %}
```

- Inside `hello_world/templates/hello_world.html` add the following

```html
{% extends "base.html" %}

{% block page_content %}
<h1>Hello, World!</h1>
{% endblock %}
```

What happens here is that any HTML inside the page_content block gets added inside the same block in `base.html`.

This will then show up in every page that extends `base.html`.

We now need to tell our our Django project that `base.html` exists. The default settings register template directories in each app, but not in the project directory itself.

In `personal_portfolio/settings.py`, update `TEMPLATES` list

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "personal_portfolio/templates/"
        ],  # register template directories inthe project directory itself
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
```

## Add styling to app

We are going to add `Bootstrap`, or any classless CSS to the entire project.

Add the stylesheet inside `base.html`'s `page_content` block.

Visiting `localhost:8000`, should show that the page has been formatted with slightly different styling.



## Additional Information

### Screenshots

### Links

## Notes template

```python
```

In the console, run the command ``

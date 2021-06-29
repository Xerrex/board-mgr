## Django Boards
* A Django Boards app where you can create boards.
* My Introduction to Django thanks to [this series](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).

## Language & tools used.
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Django](https://www.djangoproject.com/)** -  A high-level Python Web framework that encourages 
rapid development and clean, pragmatic design.
* **[Bootstrap](https://getbootstrap.com)** - he world’s most popular framework for building responsive, mobile-first sites.
* **[Docker](https://docs.docker.com/)** - An easy way to package and deploy applications.

## Table of contents

* ### [Setup](#setup)
* ### [Running](#running)
    * [Running locally](#running-locally)
    * [Running locally with docker](#running-locally-with-docker)
* ### [Testing](#testing)
    * [Local testing](#local-testing)
    * [Local testing with docker](#local-testing-with-docker)


**NB** 
* Command are for a linux based os
* Run the command after **$**:
* **$** and anything before it, shows prompt status.

## Setup

1. #### **Clone the repo.**
    ```
    $ git clone https://github.com/Xerrex/simple_project.git
    ```
2. #### change into the cloned directory
    ```
    $ cd simple_project
    ```
3. #### **Create virtual environment & Activate.**
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
4. #### **Install Dependancies.**
    ```
    (venv)$ pip install -r requirements.txt
    ```
5. #### **Enviroment variables.**
    ```
    (venv)$ cp .env.examples .env_local
    (venv)$ cp .touch .env_dev
    ```
**NB**
* replace `<>` with your actual value in the .env & .envdev

6. #### **Add the following lines to .envdev file**
    ```
    SECRET_KEY="<your-selected-key"
    DEBUG=<enter-1-or-0>
    DJ_ALLOWED_HOSTS=<list-your-host-space-separated>
    ```

## Running
### Running locally
1. * #### **Intialize schema/ database tables**
    ```
    (venv)$ python manage.py migrate
    ``` 
2. * #### **Run the app with development server**
    ```
    (venv)$ python manage.py runserver
    ```

### Running locally with docker
1. * #### **Build the container**
    ```
    $ docker-compose build
    ```
2. * #### **RUN the containners**
    ```
    $ docker-compose up
    ```
3. * #### **Intialize schema/ database tables**
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```

## Testing
### Local testing
```
(venv)$ python manage.py test
```
### Local testing with docker
```
$ docker-compose exec web python manage.py test
```
* **ensure you are in the same directory as the docker-compose.yml**
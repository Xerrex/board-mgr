# Board Manager
* Discuss your topics in an orderly manner.

## Features
* Boards - Collection of topics.
* Topics - An item worth reading about.
* Post - An Article in regards to a topic.

## Built With
* **[Python (3.8.10)](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Django (3.2.7)](https://www.djangoproject.com/)** -  A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* **[Bootstrap (5.1)](https://getbootstrap.com)** - The world’s most popular framework for building responsive, mobile-first sites.

## Table of contents

* ### [Setup](#setup)
* ### [Running](#running)
    * [Running locally](#running-locally)
    * [Running locally with docker](#running-locally-with-docker)
* ### [Testing](#testing)
    * [Local testing](#local-testing)
    * [Local testing with docker](#local-testing-with-docker)
* ### [Acknowledgement](#acknowledgement)


**NB** 
* Commands are linux based os.
* Run the command after **$**:
* **$** and anything before it, shows prompt status.

## Setup

1. #### **Clone the repo.**
    ```
    $ git clone https://github.com/Xerrex/board-mgr.git
    ```
2. #### change into the cloned directory
    ```
    $ cd board-mgr
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
    (venv)$ cp .env.examples .env
    ```
**NB**
* replace `<>` with your actual value in the .env

6. #### **Edit the following lines in .env file.**
    ```
    export SECRET_KEY="<Put your most secure key here>"
    export DEBUG=<change to True or FALSE>
    ```
7. #### **Export/Set the .env files.**
    ```
    (venv)$ source .env
    ```

## Running
### Running locally
1. * #### **Intialize schema/ database tables.**
    ```
    (venv)$ python manage.py migrate
    ``` 
2. * #### **Run the app with development server**
    ```
    (venv)$ python manage.py runserver
    ```

## Testing
### Local testing
```
(venv)$ python manage.py test
```

## Acknowledgement
* [Django Beginners Guide by Vitor Freitas](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)
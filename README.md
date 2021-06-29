## Django Boards
* A Django Boards app where you can create boards.
* My Introduction to Django thanks to [this series](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).

## Language & tools used.
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Django 2.2.4](https://www.djangoproject.com/)** -  A high-level Python Web framework that encourages 
rapid development and clean, pragmatic design.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[Bootstrap](https://getbootstrap.com)** - he world’s most popular framework for building responsive, mobile-first sites.

## Installation and usage

**NB** 
* Run the command after **$**:
* **$** and anything before it, shows prompt status.

1. #### **Clone or download repo.**
    ```
    $ git clone git@github.com:Xerrex/django_boards_project.git
    ```
2. #### **Create virtual environment & Activate.**
    ```
    $ virtualenv -p python3.6 venv 
    $ source venv/bin/activate
    ```
3. #### **Install Dependancies.**
    ```
    (venv)$ pip install -r requirements.txt
    ```
4. #### **Enviroment variables.**

    ```
    (venv)$ cp .env.examples .env
    ```
    * **Add the following lines to .env file**
        * replace [] with your actual value
    ```
    
    * You can now run **source .env** to:
      * activate virtual enviroment
      * export the SECRET_KEY 

5. #### **Intialize schema/ database tables**
   ```
   (venv)$ python manage.py migrate
   ``` 
6. #### **Run the app with development sever**
   ```
   (venv)$ python manage.py runserver
   ```
   and follow instructions.
   
7. #### **Run Tests**
   ```
   (venv)$ python manage.py test
   ```
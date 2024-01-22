# flask_crud
Simple CRUD project using Flask and SQLite for data persistence (SQLAlchemy)
This flask_crud project was created for a job challenge, this application does a simple HTTP requests in order to read or populate a database.

Git Rep: https://github.com/tikiwon/flask_crud

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python and pip (last release)
* You have a Windows machine
* You have any Python supported IDE, such as PyCharm
* You have installed the latest version of every content inside requirements.txt (pip install -r .\requirements.txt)
* You have installed virtual environment “base” Python: "venv"
* You have installed any API platform for building and using APIs: POSTMAN (https://learning.postman.com/docs/getting-started/installation/installation-and-updates/#install-postman-on-windows)

## Installing flask_crud project

To install flask_crud, follow these steps:

```
Option 1:

Install all content from requirements.txt: "pip install -r .\requirements.txt"
Install the virtual environment by using the command inside your terminal: "python -m venv venv"
Note: If you're using pyCharm it will activate the environment for you, if using other IDE, use the website below to activate it:
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
Optional: For testing, install: "pip install pytest" and "pip install pytest-flask"

------------

Option 2 (install requirements separately):

Install Flask: "pip install flask"
Install SQLAlchemy: "pip install Flask-SQLAlchemy"
Install the virtual environment by using the command: python -m venv venv
Note: If you're using pyCharm it will activate the environment for you, if using other IDE, use the website below to activate it:
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html
Optional: For testing, install: "pip install pytest" and "pip install pytest-flask"

```
## Using flask_crud project

To run the flask_crud, follow these steps:

```

1 - Start the project with run.py
2 - Open POSTMAN and choose which operation you would like to do (GET all or GET specific user):
2.1 - If you want to see all the users from the database type http://127.0.0.1:5000/users inside your browser.
2.2 - If you want to see a specific user, type the id number after /users/<id number>, ex: http://127.0.0.1:5000/users/1
3 - If you want to ADD a new User, UPDATE, or DELETE open the POSTMAN to send an API request with a JSON format.
3.1 - If you want to ADD a new User, select as a POST request, build the body with JSON format, inserting id, username, and email parameters. 
After that send it to the endpoint: 127.0.0.1:5000/users.
3.2 - If you want to update a user, select as PUT request, build the body with JSON format, inserting username, and email parameters.
after that send it to the endpoint: 127.0.0.1:5000/users/<id number that you want to update, make sure that the user exists inside the database> - Ex: 127.0.0.1:5000/users/1
3.3 - Lastly, if you want to delete a existing user, select as DELETE request, 
and send it to the ednpoint: 127.0.0.1:5000/users/<id number that you want to delete, make sure that the user exist insde the database> - Ex: 127.0.0.1:5000/users/1

```
## Using test_users project

To run the test_users, follow these steps:

```
Option 1:

1 - First, delete the directory called: instance
2 - Run the file "test_users.py", if all 5 test have passed the test the project is running correctly.

or

Option 2 (Terminal command):

1 - First, delete the directory called: instance
2 - Run the application by using this command: "pytest tests/test_users.py", if all 5 test have passed the test the project is running correctly.

```

## Contact

If you want to contact me you can reach me at <tikiwon@gmail.com>.
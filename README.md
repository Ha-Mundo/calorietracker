# foodtracker
Application to track the daily food calorie, made with python, sqlalchemy and sqlite.

1- Create a virtual enviroment: python -m venv env

2- install all the dependencies and packages: pip install requirements.txt

3- open the python shell: 1) python
                          2) from foodtraker import create_app
                          3) from foodtracker.extensions import db
                          4) db.create_all(app=create_app())
                          5) exit()

4) flask run


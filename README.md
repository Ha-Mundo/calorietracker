# foodtracker
Application to track the daily food calorie, made with python, sqlalchemy and sqlite.

1- Create a virtual enviroment: python -m venv env

2- Install all the dependencies and packages: pip install requirements.txt

3- Open the python shell: 1) python

                          2) from foodtracker import create_app
                          
                          3) from foodtracker.extensions import db

                             from foodtracker.models import log_food, Food, Log
                             
                          4) db.create_all(app=create_app())
                          
                          5) exit()

4) flask run


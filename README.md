
# Calorie Tracker
Application to track the daily food calorie, made with python, flask-sqlalchemy.

1- Create a virtual enviroment: python -m venv env

2- Install all the dependencies and packages: pip install requirements.txt

3- Open the python shell: 1) python

                          2) from calorietracker import create_app
                          
                          3) from calorietracker.extensions import db

                             from calorietracker.models import log_food, Food, Log
                             
                          4) db.create_all(app=create_app())
                          
                          5) exit()

4) flask run

# Here the the 0.1 version: https://calorie-tracker-production-d19f.up.railway.app/


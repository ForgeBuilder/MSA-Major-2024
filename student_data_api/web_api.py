import flask
from flask import request, jsonify
import classroomV2 as sg


# print(sg.get_student_dictionary())

app = flask.Flask(__name__)

#create 2 routes

#auto reload server when new changes

app.config["DEBUG"] = True

student_dictionaries = sg.get_student_dictionary()

@app.route('/',methods=['GET'])
def index():
    return "<h1>Hellow World<h1> <h1>Hellow World<h1> <h1>Hellow World<h1>"

app.run(port=5000)



































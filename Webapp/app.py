from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


app.config["SECRET_KEY"] = "your secret key"

def get_json_data(url):

    responce = requests.get(url)

    responce_json = responce.json() #ensure filetype is json

    return responce_json


@app.route("/",methods=['GET'])
def index():
    #get data
    #send data to veiwer

    url = "http://127.0.0.1:5010/api/students/all"

    student_data = get_json_data(url)

    return render_template('index.html',student_data=student_data)

@app.route("/majors",methods=['GET'])
def majors():
    return render_template('majors.html')




app.run(port=5005)
















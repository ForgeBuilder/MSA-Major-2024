from flask import Flask, render_template, request, url_for, redirect, abort, flash, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


app.config["SECRET_KEY"] = "your secret key"

def get_json_data(url):

    responce = requests.get(url)

    responce_json = responce.json() #ensure filetype is json

    return responce_json

def get_majors(url):
    major_list = []

    student_data = get_json_data(url)

    for student in student_data:
        major_to_check = student["major"]
        if not major_to_check in major_list:
            major_list.append(major_to_check)
    
    return major_list


@app.route("/",methods=['GET'])
def index():
    #get data
    #send data to veiwer

    url = "http://127.0.0.1:5010/api/students/all"

    student_data = get_json_data(url)

    return render_template('index.html',student_data=student_data)

@app.route("/majors",methods=['GET'])
def majors():

    url = "http://127.0.0.1:5010/api/students/all"

    major_list = get_majors(url)
    

    return render_template('majors.html',major_list=major_list) #send variable to templete webpage thingy

@app.route('/majors',methods=['POST'])
def majors_post():
    url = "http://127.0.0.1:5010/api/students/all"
    major_list = get_majors(url)

    #get form data
    #reject if invalid data, show error

    chosen_major = request.form.get('major')
    
    # print(chosen_major)

    result_list = []

    if not chosen_major in major_list:
        flash("You must selet a Major!")
    else:
        student_data = get_json_data(url)

        

        for student in student_data:
            if student["major"] == chosen_major:
                result_list.append(student)
    
    return render_template('majors.html',result_list=result_list,major_list=major_list)



app.run(port=5005)
















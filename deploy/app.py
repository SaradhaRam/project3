# import necessary libraries
from models import create_classes
import os
import sqlite3
from flask import Flask, redirect, render_template,url_for, request

# from flask import (
#     Flask,
#     render_template,
#     jsonify,
#     request,
#     redirect,
#     url_for)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///app.db"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Patient = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    print ("inside route /")
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["POST","GET" ])
def send():
    print("inside route /send")
    if request.method == "POST":
        age = request.form["age"]
        sex = request.form["sex"]
        cp = request.form["cp"]
        trestbps = request.form["restbpm"]
        chol = request.form["chol"]
        fbs = request.form["fbs"]
        restecg = request.form["ecg"]
        thalach = request.form["maxhr"]
        exang = request.form["exang"]
        oldpeak = request.form["oldpeak"]
        slope = request.form["slope"]
        ca = request.form["ca"]

        # patient = Patient(age=age, sex = sex, cp = cp,trestbps=trestbps,
        # chol=chol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca)
        # db.session.add(patient)
        # db.session.commit()

          # call the method to store the data in database(sqlite)
        store_patient(age, sex, cp, trestbps,chol, fbs, restecg, thalach, exang, oldpeak, slope, ca)

        # return redirect(url_for('patients'))
        return redirect('/api/patients')
    return render_template('form.html')
        # return redirect(url_for('/'))
   


        # return render_template("form.html")


@app.route("/api/patients")
def patients():
    print("inside route /api/patients")
    # results = db.session.query(Patient.age).all()
    

    return 'yoyoy'



################## Function ##########

def store_patient(age, sex, cp, trestbps,chol, fbs, restecg, thalach, exang, oldpeak, slope, ca):
    print("hello")
    connection = sqlite3.connect("C:/Users/vijay/Documents/Saradha_R/project3/project3/deploy/app.db") 
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
    insert into patients
    values (?,?,?,?,?,?,?,?,?,?,?,?)
    """, (age, sex, cp, trestbps,chol, fbs, restecg, thalach, exang, oldpeak, slope, ca))
  

    connection.commit()
    connection.close()
    return ""


##########


if __name__ == "__main__":
    app.run(debug= True)

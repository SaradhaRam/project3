# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Patient = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
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

        patient = Patient(age=age, sex = sex, cp = cp,trestbps=trestbps,
        chol=chol,fbs=fbs,restecg=restecg,thalach=thalach,exang=exang,oldpeak=oldpeak,slope=slope,ca=ca)
        db.session.add(patient)
        db.session.commit()
        return redirect("/api/patients")

    return render_template("form.html")


@app.route("/api/patients")
def patients():
    results = db.session.query(Patient.age).all()

    return 'yoyoy'


if __name__ == "__main__":
    app.run()

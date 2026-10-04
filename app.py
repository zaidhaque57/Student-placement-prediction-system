from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/placement_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    assignment_score = float(request.form["assignment_score"])
    internal_marks = float(request.form["internal_marks"])
    previous_percentage = float(request.form["previous_percentage"])

    data = [[
        study_hours,
        attendance,
        assignment_score,
        internal_marks,
        previous_percentage
    ]]

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Student is likely to be PLACED ✅"
    else:
        result = "Student is likely to be NOT PLACED ❌"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
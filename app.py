from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -------------------------
# Simple AI Logic
# -------------------------
def predict_job(skills, experience):

    skills = skills.lower()

    if "python" in skills and "machine learning" in skills:
        return "AI / ML Engineer"
    elif "html" in skills and "css" in skills and "javascript" in skills:
        return "Frontend Developer"
    elif "sql" in skills and "database" in skills:
        return "Database Engineer"
    elif "java" in skills:
        return "Java Developer"
    elif "network" in skills:
        return "Network Administrator"
    else:
        return "Software Developer"

# ------------------------
# ROUTES
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["resume"]
    skills = request.form["skills"]
    exp = request.form["experience"]

    # Save resume
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    # AI Prediction
    prediction = predict_job(skills, exp)

    return render_template("result.html",
                           prediction=prediction,
                           skills=skills,
                           exp=exp)

if __name__ == "__main__":
    app.run(debug=True)

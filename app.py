from flask import Flask, render_template, request,redirect,url_for
import pickle

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid Username or Password")

    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["job_description"]
    text_vector = tfidf.transform([text])
    prediction = model.predict(text_vector)

    if prediction[0] == 1:
        result = "Fake Job Posting"
    else:
        result = "Real Job Posting"

    return render_template("index.html", prediction=result, job_description=text)

if __name__ == "__main__":
    app.run(debug=True)

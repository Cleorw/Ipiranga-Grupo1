from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agradecimento")
def agradecimento():
    return render_template("agradecimento.html")

@app.route("/form1")
def form1():
    return render_template("form1.html")

@app.route("/form1submit", methods=["POST"])
def form1submit():
    gender = request.form["gender"]
    age = request.form["age"]
    region = request.form["region"]
    expense = request.form["expense"]
    app_use = request.form["app_use"]
    with open("data.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([gender, age, region, expense, app_use])
    if app_use == "Sim":
        return redirect("/form2")
    else:
        return redirect("/agradecimento")

@app.route("/form2")
def form2():
    return render_template("form2.html")

@app.route("/form2submit", methods=["POST"])
def form2submit():
    convenience = request.form["convenience"]
    payment_app = request.form["payment_app"]
    recommend = request.form["recommend"]
    with open("data.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([convenience, payment_app, recommend])
    return redirect("/agradecimento")

@app.route("/form2-1")
def form2_1():
    return render_template("form2-1.html")

@app.route("/form2-1submit", methods=["POST"])
def form2_1submit():
    obstacle = request.form["obstacle"]
    change_mind = request.form["change_mind"]
    with open("data.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([obstacle, change_mind])
    return redirect("/agradecimento")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form['name']
        app_usage = request.form['answer']
        if app_usage == 'yes':
            return redirect('/survey2')
        else:
            return redirect('/survey2_1')
    return render_template('survey.html')

@app.route('/survey2', methods=['GET', 'POST'])
def survey2():
    if request.method == 'POST':
        payments = request.form['payments']
        discounts = request.form['discounts']
        convenience_store = request.form['convenience_store']
        return redirect('/thankyou')
    return render_template('survey2.html')

@app.route('/survey2_1', methods=['GET', 'POST'])
def survey2_1():
    if request.method == 'POST':
        obstacles = request.form['obstacles']
        reconsideration = request.form['reconsideration']
        recommend = request.form['recommend']
        return redirect('/thankyou')
    return render_template('survey2_1.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

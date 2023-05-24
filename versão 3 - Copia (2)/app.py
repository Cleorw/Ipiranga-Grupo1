from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form['name']
        return redirect('/survey2')
    return render_template('survey.html')

@app.route('/survey2', methods=['GET', 'POST'])
def survey2():
    if request.method == 'POST':
        app_usage = request.form['app_usage']
        if app_usage == 'yes':
            return redirect('/thankyou')
        else:
            return redirect('/survey2_1')
    return render_template('survey2.html')

@app.route('/survey2_1', methods=['GET', 'POST'])
def survey2_1():
    if request.method == 'POST':
        payments = request.form['payments']
        discounts = request.form['discounts']
        convenience_store = request.form['convenience_store']
        return redirect('/thankyou')
    return render_template('survey2_1.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

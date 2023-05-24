from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        usa_app = request.form.get('usa_app')

        if usa_app == 'Sim':
            return render_template('questionario.html')
        else:
            return render_template('outro_questionario.html')

    return redirect('/')

@app.route('/agradecimento', methods=['POST'])
def agradecimento():
    respostas = []
    respostas.append(request.form.get('usa_pagamentos'))
    respostas.append(request.form.get('usa_descontos'))
    respostas.append(request.form.get('usa_conveniencia'))
    
    with open('respostas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(respostas)

    return render_template('agradecimento.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o questionário
@app.route('/questionario', methods=['GET', 'POST'])
def questionario():
    if request.method == 'POST':
        nome = request.form['nome']
        app_uso = request.form['app_uso']
        app_pagamentos = request.form.get('app_pagamentos', '')
        app_descontos = request.form.get('app_descontos', '')
        app_compras = request.form.get('app_compras', '')
        impede_uso = request.form.get('impede_uso', '')
        mudar_ideia = request.form.get('mudar_ideia', '')
        recomendar = request.form.get('recomendar', '')

        salvar_dados(nome, app_uso, app_pagamentos, app_descontos, app_compras, impede_uso, mudar_ideia, recomendar)

        return redirect('/obrigado')  # Redireciona para a página de agradecimento

    return render_template('questionario.html')

# Rota de agradecimento
@app.route('/obrigado')
def agradecimento():
    return render_template('agradecimento.html')

def salvar_dados(nome, app_uso, app_pagamentos, app_descontos, app_compras, impede_uso, mudar_ideia, recomendar):
    with open('respostas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, app_uso, app_pagamentos, app_descontos, app_compras, impede_uso, mudar_ideia, recomendar])

if __name__ == '__main__':
    app.run(debug=True)

# http://localhost:5000/

import os
import mysql.connector
from flask import Flask, redirect, render_template, request, url_for, flash, jsonify
from lxml import etree

app = Flask(__name__, static_folder='templates')

@app.route('/')
def index():
    return redirect(url_for('cadastro_usuario'))

# rota para a página de cadastro de usuário
@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    return render_template('cadastro_usuario.html')

# rota para processar o formulário de cadastro de usuário
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':

        #Obter dados da lista de compras do formulário
        nome = request.form.getlist('nome')
        apelido = request.form.getlist('apelido')
        email = request.form.getlist('email')
        data_nascimento = request.form.getlist('data_nascimento')
        perfil = request.form.getlist('perfil')
        senha = request.form.getlist('senha')

        try:
            # Conectar ao banco de dados
            cnx = mysql.connector.connect(user='control_home', password='controlhome', host='localhost', database='control_home')

            cursor = cnx.cursor()

            # Adicionar novo usuário à tabela de Usuário
            query = "INSERT INTO Usuario (Nome, Apelido, Email, DataNascimento, Perfil, Senha) VALUES (%s, %s, %s, %s, %s, %s)"
            
            values = (nome, apelido, email, data_nascimento, perfil, senha)

            # Gravar dados no banco de dados
            cnx.commit()

            # Fechar conexão com o banco de dados
            cursor.close()
            cnx.close()

            return redirect(url_for('cadastro_usuario'))
        except mysql.connector.Error as error:
            print("Falha ao inserir os dados do usuário: {}".format(error))
            return "Erro ao inserir os dados do usuário"

if __name__ == '__main__':
    app.run(debug=True)
    

    
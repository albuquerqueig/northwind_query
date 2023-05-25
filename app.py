from flask import Flask, render_template, request, session, flash, url_for, redirect
from flask_mysqldb import MySQL

class Users:
    def __init__(self, nome, nickname, senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

user1 = Users("Guest", "guest", "1234")
user2 = Users("Guest", "guest", "1234")
user3 = Users("Guest", "guest", "1234")

usuarios = { user1.nickname : user1,
             user2.nickname : user2,
             user3.nickname : user3}

app = Flask(__name__)

app.config['SECRET_KEY'] = '21051999'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ab1234##'
app.config['MYSQL_DB'] = 'northwind'

mysql = MySQL(app)

# Rota da páginad e login
@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

# Rota de autenticação de dados de acesso
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado!')
            proxima_pagina = request.form['proxima']
            return redirect(url_for('customers'))
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('login'))

# Rota de direcionamento para a página HOME que terá todas as funcionalidades CRUD
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'create':
            # Obtém os dados do formulário
            company = request.form['company']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            job_title = request.form['job_title']
            address = request.form['address']

            # Insere os dados no banco de dados
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO customers (company, first_name, last_name, job_title, address) VALUES (%s, %s, %s, %s, %s)", (company, first_name, last_name, job_title, address))
            mysql.connection.commit()
            cur.close()

            flash('Novo cliente criado com sucesso!')
            return redirect(url_for('customers'))

        elif action == 'update':
            id = request.form['id']
            company = request.form['company']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            job_title = request.form['job_title']
            address = request.form['address']

            # Atualiza os dados no banco de dados
            cur = mysql.connection.cursor()
            cur.execute("UPDATE customers SET company=%s, first_name=%s, last_name=%s, job_title=%s, address=%s WHERE id=%s", (company, first_name, last_name, job_title, address, id))
            mysql.connection.commit()
            cur.close()

            flash('Cliente atualizado com sucesso!')
            return redirect(url_for('customers'))


        elif action == 'delete':
            # Obtém o ID do cliente
            id = request.form['id']

            # Exclui o cliente do banco de dados
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM customers WHERE id = %s", (id,))
            mysql.connection.commit()
            cur.close()

            flash('Cliente deletado com sucesso!')
            return redirect(url_for('customers'))

    # Se não for uma requisição POST, exibe a lista de clientes
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, company, first_name, last_name, job_title, address FROM northwind.customers")
    customers_data = cur.fetchall()
    cur.close()
    return render_template('customers.html', customers=customers_data)

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Usuário deslogado!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
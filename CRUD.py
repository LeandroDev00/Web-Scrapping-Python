#importando SQLITE
import sqlite3 as conector

#Criando Conexão
conexao = conector.connect('vinhos.db')

#Inserir Produtos
def inserir_prod(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO PRODUTOS (Produto, Preco, Tipo, Regiao, Graduacao) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, i)

#Inserir Usuário
def inserir_user(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO USUARIO (Nome, Email, Senha, ConfirmaSenha) VALUES (?, ?, ?, ?)"
        cursor.execute(query, i)

#Mostrar todos o Dados
def mostrar_dados():
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM PRODUTOS"
        cursor.execute(query)
        for informacao in cursor.fetchall():
            print(informacao)

def editar_dados(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE PRODUTOS set PRODUTO =? WHERE ID=?"
        cursor.execute(query, i)
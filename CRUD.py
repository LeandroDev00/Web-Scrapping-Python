#importando SQLITE
import sqlite3 as conector

#Criando Conexão
conexao = conector.connect('vinhos.db')

#Inserir Produtos (INSERT)
def inserir_prod(dados):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO PRODUTOS (Produto, Preco, Tipo, Regiao, Graduacao) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, dados)



#Atualizar dados (UPDATE)
def atualizar_dados(id):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE PRODUTOS set Produto=?, Preco=?, Tipo=?, Regiao=?, Graduacao=? WHERE IDProduto=?"
        cursor.execute(query, id)

#Excluir Produto (DELETE)
def delete_dados(id):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM PRODUTOS WHERE IDProduto=?"
        cursor.execute(query, id)

#Mostrar todos o Dados (SELECT)
def mostrar_dados():
    dados = []
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM PRODUTOS"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            dados.append(row)
    return dados

def visual_dado(id):
    dados_indi = []
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM PRODUTOS WHERE IDproduto=?"
        cursor.execute(query, id)
        rows = cursor.fetchall()
        for row in rows:
            dados_indi.append(row)
    return dados_indi

#--------------------------------------------------------------------------------------------------------------

#Inserir Usuário (INSERT)
def inserir_user(dados):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO USUARIO (Nome, Email, Senha, ConfirmaSenha) VALUES (?, ?, ?, ?)"
        cursor.execute(query, dados)

def consulta_user(login, senha):
    with conexao:
        cursor = conexao.cursor()
        query = "SELECT * FROM USUARIO WHERE Nome = ? AND Senha = ?"
        cursor.execute(query, (login, senha))
        rows = cursor.fetchall()
        for row in rows:
            return row
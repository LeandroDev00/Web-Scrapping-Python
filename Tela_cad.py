from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#importando CRUD
from CRUD import *

def cadastrar_produto():

    Produto = produtoinput.get()
    Preco = precoinput.get()
    Tipo = tipoinput.get()
    Regiao = regiaoinput.get()
    Graduacao = graduacaoinput.get()

    lista = [Produto, Preco, Tipo, Regiao, Graduacao]
            
    if Produto == "" and Preco == "" :
         messagebox.showerror(title="Erro", message="Erro ao cadastrar Produto.")
    else:
        inserir_prod(lista)
        messagebox.showinfo(title="Informação", message="Cadastro com Sucesso")

    produtoinput.delete(0, "end")
    precoinput.delete(0, "end")
    tipoinput.delete(0, "end")
    regiaoinput.delete(0, "end")
    graduacaoinput.delete(0, "end")

def editar_prod():
    Produto = produtoinput.get()
    Preco = precoinput.get()
    Tipo = tipoinput.get()
    Regiao = regiaoinput.get()
    Graduacao = graduacaoinput.get()

    lista = [Produto, Preco, Tipo, Regiao, Graduacao]
    if editar_dados(lista):
        messagebox.showinfo(title="Informação", message="Edição com Sucesso")
    else:
        messagebox.showerror(title="Error Editor", message="Edição sem sucesso, verifique novamente.")

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

root = Tk()

root.title("Cadastre seu produto")
root.geometry("930x589")
root.resizable(TRUE,TRUE)

#PRODUTO#
produto = Label(root, text="Produto :")
produto.grid(column=1, row=0, padx=1, pady=10)

produtoinput = Entry(root, text="produto", border=2)
produtoinput.grid(column=2, row=0, padx=10, pady=10)

#TIPO#
tipo = Label(root, text="Tipo :")
tipo.grid(column=1, row=1, padx=10, pady=10)

tipoinput = Entry(root, text="tipo", border=2)
tipoinput.grid(column=2, row=1, padx=10, pady=10)

#PRECO#
preco = Label(root, text="Preço :")
preco.grid(column=4, row=0, padx=10, pady=10)

precoinput = Entry(root, text="preco", border=2)
precoinput.grid(column=5, row=0, padx=10, pady=10)

#GRADUAÇÃO#
graduacao = Label(root, text="Graduação% :", )
graduacao.grid(column=4, row=1, padx=10, pady=10)

graduacaoinput = Entry(root, text="graduacao", border=2)
graduacaoinput.grid(column=5, row=1, padx=10, pady=10)

#REGIAO#
regiao = Label(root, text="Regiao :")
regiao.grid(column=4, row=2, padx=10, pady=10)

regiaoinput = Entry(root, text="regiao", border=2)
regiaoinput.grid(column=5, row=2, padx=10, pady=10)

#BOTOES#
cadastro = Button(root, text= " Cadastrar ", command=cadastrar_produto) 
cadastro.grid(column=2, row=6, padx=10, pady=10)

editar = Button(root, text= "  Editar  ", command=editar_prod) 
editar.grid(column=3, row=6, padx=10, pady=10)

limpar = Button(root, text= "  Limpar  ") 
limpar.grid(column=4, row=6, padx=10, pady=10)

tabelagrid = ['ID', 'Produto', 'Preço', 'Tipo', 'Região', 'Graduação%']

'''
frame_baixo = Frame(root,width=100, height=50)
frame_baixo.grid(column=2, row=8, padx=1, pady=2)
tree = ttk.Treeview(frame_baixo, selectmode='extended', columns=tabelagrid)
tree.grid(column=0, row=8)
'''
root.mainloop()

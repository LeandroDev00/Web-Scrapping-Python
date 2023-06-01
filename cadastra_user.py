from tkinter import messagebox
from tkinter import *
import re
from CRUD import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", "10")

        self.primeiroContainer = Frame(master, pady=10)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, padx=20, pady=5)
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master, padx=20, pady=5)
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master, padx=20, pady=5)
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master, padx=20, pady=5)
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master, padx=20, pady=5)
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master, padx=20, pady=5)
        self.setimoContainer.pack()

        self.oitavocontainer = Frame(master, pady=15)
        self.oitavocontainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Cadastro cliente:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblnome = Label(self.terceiroContainer, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.terceiroContainer, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lblemail= Label(self.quartoContainer, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.quartoContainer, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblsenha= Label(self.quintoContainer, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.quintoContainer, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

        self.lblconfirmaSenha= Label(self.sextoContainer, text="Confirma Senha:", font=self.fonte, width=14)
        self.lblconfirmaSenha.pack(side=LEFT)

        self.txtconfirmaSenha = Entry(self.sextoContainer, width=25, show="*", font=self.fonte)
        self.txtconfirmaSenha.pack(side=LEFT)

        self.bntInsert = Button(self.setimoContainer, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)

        self.lblmsg = Label(self.oitavocontainer, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

    def validar_email(self, email):
        padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\.br$"
        return re.match(padrao, email) is not None

    def inserirUsuario(self):
        nome = self.txtnome.get()
        email = self.txtemail.get()
        senha = self.txtsenha.get()
        confirmaSenha = self.txtconfirmaSenha.get()
        usuario = [nome, email, senha, confirmaSenha]  # Pass individual arguments, not a list
        if self.validar_email(email):
            if senha == confirmaSenha and senha and confirmaSenha != '':
                if nome != '':
                    inserir_user(usuario)
                    messagebox.showinfo(title="Usuário", message="Usuário inserido com sucesso!!")
                    self.txtnome.delete(0, END)
                    self.txtemail.delete(0, END)
                    self.txtsenha.delete(0, END)
                    self.txtconfirmaSenha.delete(0, END)
                else:
                    messagebox.showerror(title="Usuário", message="Erro insira o nome do usuário!")
            else:
                messagebox.showerror(title="Usuário", message="As senhas não coincidem!")
        else:
            messagebox.showerror(title="Usuário", message="E-mail inválido!")
root = Tk()
Application(root)
root.mainloop()
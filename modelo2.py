
from tkinter import messagebox
from tkinter import *
from CRUD import *


class Application:
    def __init__(self, master=None):
#inicio do Formulario de Usuario

        #definição dos containers
        self.fonte = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["pady"] = 5
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer["pady"] = 5
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 20
        self.setimoContainer["pady"] = 5
        self.setimoContainer.pack()

        self.oitavocontainer = Frame(master)
        self.oitavocontainer["pady"] = 15
        self.oitavocontainer.pack()

    #especifição dos containers

        #Titulo
        self.titulo = Label(self.primeiroContainer, text="Cadastro cliente: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
        '''
        #idusuario
        self.lblidusuario = Label(self.segundoContainer,
        text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.segundoContainer)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        '''
        #Nome
        self.lblnome = Label(self.terceiroContainer, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.terceiroContainer)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
        #E-mail
        self.lblemail= Label(self.quartoContainer, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.quartoContainer)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)
        #Senha
        self.lblsenha= Label(self.quintoContainer, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.quintoContainer)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)
        #Confirmar Senha
        self.lblconfirmaSenha= Label(self.sextoContainer, text="Confirma Senha:",
        font=self.fonte, width=11)
        self.lblconfirmaSenha.pack(side=LEFT)

        self.txtconfirmaSenha = Entry(self.sextoContainer)
        self.txtconfirmaSenha["width"] = 25
        self.txtconfirmaSenha["show"] = "*"
        self.txtconfirmaSenha["font"] = self.fonte
        self.txtconfirmaSenha.pack(side=LEFT)
        #interativos bd
        self.bntInsert = Button(self.setimoContainer, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)
       
        self.lblmsg = Label(self.oitavocontainer, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

#Fim do Formulario de Usuario

    def inserirUsuario(self):

        nome = self.txtnome.get()
        email = self.txtemail.get()
        senha = self.txtsenha.get()
        confirmaSenha = self.txtconfirmaSenha.get()

        lista = [nome, email, senha, confirmaSenha]

        if inserir_user(lista):
            messagebox.showinfo(title="Usuário", Message="Usuário inserido com sucesso!")
        else:
             messagebox.showerror(title="Usuário", Message="Dados inválidos !")

        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtconfirmaSenha.delete(0, END)

root = Tk()
Application(root)
root.mainloop()
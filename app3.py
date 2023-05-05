from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from tkinter import messagebox
from tkinter import *
import sqlite3 as conector
import time
import re

try:
    #abertura de conexão SQLITE 
    conexao = conector.connect("vinhos.db")
     

    # Execução de um comando: SELECT ... CREATE
    def imprimir_prod():

        # Aquisição de um cursor
        cursor = conexao.cursor()

        selecao_vinhos = '''SELECT * FROM MERCADORIA'''
        cursor.execute(selecao_vinhos)
        for linha in cursor.fetchall():
            print(linha)
            #impressao = f'''
            #                produtos:{linha}
            #            '''
            #listatxt["Text"] = impressao

        cursor.close()

    def requisicao():

        url = "http://www.vinhosevinhos.com/"

        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)

        driver.get(url)
        time.sleep(10)


        driver.find_element(by=By.XPATH, value="/html/body/div[5]/main/div[2]/div/div[4]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]")
    
        busca = driver.find_element(By.XPATH, "/html/body/div[5]/main/div[2]/div/div[4]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]")
        htmlbusca = busca.get_attribute('outerHTML')

        #Utilizando a biblioteca BeautifulSoup para facilitar a busca de elementos HTML
        produtos = BeautifulSoup(htmlbusca, 'html.parser')

        for produto in produtos:
            descricao = produto.find_all_next("a", attrs={'class': re.compile('product-item-link')})
            preco = produto.find_all("span", attrs={"class" : re.compile("price-wrapper")})

        descrivinho = descricao[0].contents[0].text
        precovinho = preco[0].contents[0].text
    
        print(descrivinho)
        print(precovinho)
    
        driver.quit()

    def busca_produto():

        janela = Tk()
        janela.title("Vinicula Web - Monitoramento de Produtos ")
        janela.geometry("500x300")

        inserir = Label(janela, text="Insira um Produto")
        inserir.grid(column=1, row=0, padx=10, pady=10)

        cx_inserir = Entry(janela, text="Insira um Produto")
        cx_inserir.grid(column=2, row=0, padx=10, pady=10)

        botao = Button(janela, text= "buscar produto Web", command=requisicao) 
        botao.grid(column=1, row=1, padx=10, pady=10)

        imprimir = Button(janela, text= "imprimir produtos", command=imprimir_prod) 
        imprimir.grid(column=2, row=1, padx=10, pady=10)

        listatxt = Label(janela, text = "")
        listatxt.grid(column=4, row=2, padx=30, pady=30)

        janela.mainloop()    

    #Efetivação do comando
    conexao.commit()

#Exceção de erro 
except conector.DatabaseError as err:
    print("Erro ao abrir o banco de dados: %s" % err)


#Fecha conexão SQLITE
    conexao.close()
 
#Requests - Biblioteca Python para requisições HTTP

###### Inicio tela de Login ######
# cores -----------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
    # criando janela --------------------

janela = Tk ()
janela.title ("")
janela.geometry('400x410')
janela.configure(background=co1)
janela.resizable(width=TRUE, height=TRUE)


    ################# Frames ####################

frame_cima = Frame(janela,width=310, height=50,bg=co1, relief="flat")
frame_cima.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(janela,width=310, height=300,bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

    # configurando frame_cima
l_nome = Label(frame_cima, text="LOGIN", height=1,anchor=NE, font=('Ivy 25 '), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=co2)
l_linha.place(x=10, y=45)

    # configurando frame_baixo ---------------------------

l_nome = Label(frame_baixo, text="Nome *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left',font=("",15),highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="password *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo,show='*',width=25, justify='left',font=("",15),highlightthickness=1,relief="solid")
e_pass.place(x=15, y=130)

botao_confirmar = Button(frame_baixo, text="Entrar", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)

def nova_janela():
    l_nome = Label(frame_cima, text="Usuario: " + 'credenciais'[0], height=1,anchor=NE, font=('Ivy 20 '), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=co2)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text="Seja bem vindo " + 'credenciais'[0], height=1,anchor=NE, font=('Ivy 15 '), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

    ########### lógica de validação senha #############
def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome=='admin' and senha=='admin':
        messagebox.showinfo('Login',' Seja bem vindo Admin !!!')
        busca_produto()

    # verificando os dados para permitir o login do usuario
    elif 'credenciais'[0] == nome and 'credenciais'[1] == senha:
        messagebox.showinfo('Login',' Seja bem vindo de volta '+'credenciais'[0])

        # apagar o que tiver no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        # chamr nova janela
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuario ou a senha')
    ###############botão Enter##############

botao_confirmar = Button(frame_baixo, command=verificar_senha, text="Entrar", width=39, height=2, bg=co2, fg=co1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)
421

janela.mainloop()
    ########  Fim tela de Login #########
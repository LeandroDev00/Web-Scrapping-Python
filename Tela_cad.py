from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#importando CRUD
from CRUD import *
def main_cad():

    def cadastrar_produto():

        Produto = produtoinput.get()
        Preco = precoinput.get()
        Tipo = tipoinput.get()
        Regiao = regiaoinput.get()
        Graduacao = graduacaoinput.get()

        lista = [Produto, Preco, Tipo, Regiao, Graduacao]

        for i in lista:        
            if i == "" :
                messagebox.showerror(title="Erro", message="Erro, Preencha os campos!")
                return
            
        inserir_prod(lista)
        messagebox.showinfo(title="Informação", message="dados cadastrados com sucesso")

        produtoinput.delete(0, "end")
        precoinput.delete(0, "end")
        tipoinput.delete(0, "end")
        regiaoinput.delete(0, "end")
        graduacaoinput.delete(0, "end")

    def update():
        try:
            treev_dados = tree.focus()
            treev_dic = tree.item(treev_dados)
            treev_lista = treev_dic["values"]

            valor = int(treev_lista[0])

            produtoinput.delete(0, "end")
            precoinput.delete(0, "end")
            tipoinput.delete(0, "end")
            regiaoinput.delete(0, "end")
            graduacaoinput.delete(0, "end")

            id = int(treev_lista[0])
            produtoinput.insert(0, treev_lista[1])
            precoinput.insert(0, treev_lista[2])
            tipoinput.insert(0, treev_lista[3])
            regiaoinput.insert(0, treev_lista[4])
            graduacaoinput.insert(0, treev_lista[5])

            def atualizar():
                Produto = produtoinput.get()
                Preco = precoinput.get()
                Tipo = tipoinput.get()
                Regiao = regiaoinput.get()
                Graduacao = graduacaoinput.get()

                lista_atualizar = [Produto, Preco, Tipo, Regiao, Graduacao, id]

                for i in lista_atualizar:
                    if i == "" :
                        messagebox.showerror(title="Erro", message="Erro, Preencha os campos!")
                        return
                atualizar_dados(lista_atualizar)
                messagebox.showinfo(title="Informação", message="dados atualizados com sucesso")

                produtoinput.delete(0, "end")
                precoinput.delete(0, "end")
                tipoinput.delete(0, "end")
                regiaoinput.delete(0, "end")
                graduacaoinput.delete(0, "end")

                atualizar.destroy()
                dados_tabela()
                
            atualizar = Button(frame_cima, text= "  CONFIRMAR  ", command=atualizar, font=('Ivy 10 bold'), bg=co2, overrelief=RIDGE) 
            atualizar.grid(column=7, row=1, padx=10, pady=10)

        except IndexError:
            messagebox.showerror(title="Erro", message="Erro, selecione um item da lista!")

    def delete():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0]

            delete_dados([valor])
            messagebox.showinfo(title='Sucesso', message='Dados deletados com sucesso')

            dados_tabela()
        except IndexError:
            messagebox.showerror(title='Erro', message='Selecione um dos dados da tabela')

    #CONFIGURANDO TABELA GRID
    def dados_tabela():
        tabelagrid = ['ID', 'Produto', 'Preço', 'Tipo', 'Região', 'Graduação%']

        listaprod = mostrar_dados()

        global tree

        tree = ttk.Treeview(frame_baixo, selectmode="extended", columns=tabelagrid, show="headings", height=20)
        tree.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo, orient="vertical", command=tree.yview)
        vsb.grid(column=1, row=0, padx=10, pady=10, sticky='ns')

        #horizontal scrollbar
        #hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.yview)
        #hsb.grid(column=0, row=1, padx=10, pady=10)

        tree.configure(yscrollcommand=vsb.set)

        hd=["center", "center", "center", "center", "center", "center"]
        h=[40, 200, 90, 100, 200, 90]
        n=0
        for c in tabelagrid:
            tree.heading(c, text=c.title(), anchor=CENTER)
            tree.column(c, width=h[n], anchor=hd[n])
            n+=1

        for item in listaprod:
            tree.insert('', 'end', values=item)
        

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
    co10 = "#363636"  #Grey
    
    root = Tk()

    root.title("Cadastro de produto")
    root.geometry("1080x720")
    root.resizable(TRUE,TRUE)
    style = ttk.Style(root)
    style.theme_use("clam")

    # Frame parte de Cima
    frame_cima = Frame(root, width=1920, height=1080, bg=co1, relief=FLAT)
    frame_cima.grid(column=0, row=0, padx=0, pady=8)

    frame_baixo = Frame(root, width=900, height=300, bg=co1, relief=FLAT)
    frame_baixo.grid(column=0, row=1, sticky=NSEW)
    frame_baixo.grid_rowconfigure(0, weight=12)

    # -------------------------------------------------------------
    #PRODUTO#
    produto = Label(frame_cima, text="Produto :",bg=co1, font=('Ivy 10 bold'))
    produto.grid(column=1, row=0, padx=0, pady=0)

    produtoinput = Entry(frame_cima, text="produto", border=2)
    produtoinput.grid(column=2, row=0, padx=10, pady=10)

    #TIPO#
    tipo = Label(frame_cima, text="Tipo :", bg=co1, font=('Ivy 10 bold'))
    tipo.grid(column=1, row=1, padx=10, pady=10)

    tipoinput = Entry(frame_cima, text="tipo", border=2)
    tipoinput.grid(column=2, row=1, padx=10, pady=10)

    #PRECO#
    preco = Label(frame_cima, text="Preço :",bg=co1, font=('Ivy 10 bold'))
    preco.grid(column=1, row=2, padx=10, pady=10)

    precoinput = Entry(frame_cima, text="preco", border=2)
    precoinput.grid(column=2, row=2, padx=10, pady=10)

    #GRADUAÇÃO#
    graduacao = Label(frame_cima, text="Graduação% :",bg=co1, font=('Ivy 10 bold'))
    graduacao.grid(column=4, row=0, padx=10, pady=10)

    graduacaoinput = Entry(frame_cima, text="graduacao", border=2)
    graduacaoinput.grid(column=5, row=0, padx=10, pady=10)

    #REGIAO#
    regiao = Label(frame_cima, text="Região :", height=1,bg=co1, font=('Ivy 10 bold'))
    regiao.grid(column=4, row=1, padx=10, pady=10)

    regiaoinput = Entry(frame_cima, text="regiao", border=2)
    regiaoinput.grid(column=5, row=1, padx=10, pady=10)

    #BOTOES#
    cadastro = Button(frame_cima, text= " CADASTRAR ", command=cadastrar_produto, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE) 
    cadastro.grid(column=6, row=0, padx=10, pady=10)

    ver = Button(frame_cima, text= "  ATUALIZAR  ", command=update, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE) 
    ver.grid(column=6, row=1, padx=10, pady=10)

    excluir = Button(frame_cima, text= "  EXCLUIR  ", command=delete, font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE) 
    excluir.grid(column=6, row=2, padx=10, pady=10)

    limpar = Button(frame_cima, text= "  LIMPAR  ", font=('Ivy 10 bold'), bg=co1, overrelief=RIDGE) 
    limpar.grid(column=7, row=0, padx=10, pady=10)

    dados_tabela()

    root.mainloop()

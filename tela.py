import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db

#abre a janela principal
def abrir_tela():
    janela = tk.Tk()
    janela.geometry("400x320")
    janela.title("Sistema de Controle de Estoque")

    tk.Label(janela, text="Consultar Produtos", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(janela, text="Número da Loja:").pack(pady=5)
    global entrada_loja
    entrada_loja = tk.Entry(janela, font=("Arial", 12))
    entrada_loja.pack(pady=5)
    

    tk.Label(janela, text="Nome do produto:").pack(pady=5)
    global entrada_produto
    entrada_produto = tk.Entry(janela, font=("Arial", 12))
    entrada_produto.pack(pady=5)

    tk.Button(janela, text="Consultar Produtos", width=20, command=busca).pack(pady=5)
    tk.Button(janela, text="Cadastrar Produtos", width=20, command=cadastrar).pack(pady=5)

    tk.Button(janela, text="SAIR", width=20, command=janela.destroy).pack(pady=5)

    janela.mainloop()


#buscar produtos no banco de dados
def busca():
    loja = entrada_loja.get().strip()
    produto = entrada_produto.get()

    if not loja:
        print("digita o número da loja primeiro")
        alertas("Erro!", "Digite o número da loja!", "error")
        return False
    
    elif produto:
            item = db.consultar_produto(produto, int(loja))
            if item:
                tabela(item)
            else:
                alertas("Não Encontrado.", f"O Produto {produto} não foi encontrado na loja {loja}.", "info")
    else:
        todos_produtos = db.listar_produtos(int(loja))
        tabela(todos_produtos)    


#cadastrar produtos no banco de dados    
def cadastrar():
           
    cadastro = tk.Toplevel()
    cadastro.geometry("350x500")
    cadastro.title("Cadastro de Produtos no Estoque")

    tk.Label(cadastro, text="Cadastrar novo Produto").pack(pady=20)
    
    tk.Label(cadastro, text="Nome do Produto").pack(pady=5)
    global entrada_nome
    entrada_nome = tk.Entry(cadastro, font=("Arial", 12))
    entrada_nome.pack(pady=5)

    tk.Label(cadastro, text="Preço do Produto").pack(pady=5)
    global entrada_valor
    entrada_valor = tk.Entry(cadastro, font=("Arial", 12))
    entrada_valor.pack(pady=5)
    
    tk.Label(cadastro, text="Quantidade").pack(pady=5)
    global entrada_quant
    entrada_quant = tk.Entry(cadastro, font=("Arial", 12))
    entrada_quant.pack(pady=5)
    
    tk.Label(cadastro, text="Loja").pack(pady=5)
    global numero_loja
    numero_loja = tk.Entry(cadastro, font=("Arial", 12))
    numero_loja.pack(pady=5)

    
    #cria uma campo para exibir mensagens 
    msg = tk.StringVar(value="")
    tk.Label(cadastro, textvariable=msg).pack(pady=5)
   
   #atualiza o campo de texto com o a mensagem
    def mensagem(txt):
        msg.set(txt)

    #limpa os inputs após a inserção no banco
    def limpar_campos():
         numero_loja.delete(0, tk.END)
         entrada_quant.delete(0, tk.END)
         entrada_nome.delete(0, tk.END)
         entrada_valor.delete(0, tk.END)

         return 
    
    #incluir novo produto na tabela da respectiva loja
    def incluir():
            try:
                 nome = entrada_nome.get()
                 if nome == "":
                      mensagem("Nome Inválido")
                      alertas("Erro!", "Insira um nome", "warning")
                 
            except ValueError:
                print("Erro", "Nome inválido.")
                alertas("Erro!", "Nome Inválido", "warning")

            try:
                valor = float(entrada_valor.get().strip())
            except ValueError:
                print("Erro", "Preço inválido.")
                alertas("Erro.", "Preço inválido.", "warning")
                 
            
            try:
                quantidade = int(entrada_quant.get().strip())
            except ValueError:
                print("Erro", "Quantidade inválida.")
                alertas("Erro.", "Quantidade inválida.","warning")
                
            try:
                loja_text = numero_loja.get().strip()
                if loja_text not in ("1001", "1002", "1003"):
                    print("Erro", "Código da loja inválido.")
                    alertas("Erro!", "Loja Não Existe.", "warning")
                else:
                     loja_num = int(loja_text)
            except:
                    mensagem("Loja inválida.")
                    alertas("Erro!", "Loja Inválida", "error") 
            
            
            #salva o produto no db
            callback = alertas("Confirmar", "Deseja realmente incluir o item?", "yesorno")
            if callback:
                 db.cadastrar_produtos(nome, valor, quantidade, loja_num)
                 print("Sucesso", "Produto cadastrado.")
                 alertas("Sucesso.", f"O produto {nome} foi cadastrado com sucesso na loja {loja_num}.", "info")
                 limpar_campos()
            else:
                print("clicou em não")
                return False
            

            

    tk.Button(cadastro, text="Incluir", command=incluir).pack(pady=10)
    tk.Button(cadastro, text="Fechar", command=cadastro.destroy).pack()




#exibe a tabela de resultado da busca por produtos
def tabela(texto):
    resultado = tk.Tk()
    resultado.title("Produtos no Estoque")

    colunas = ("Produto", "Valor", "Quantidade", "vendidos")
    tabela = ttk.Treeview(resultado, columns=colunas, show="headings")
    for c in colunas:
        tabela.heading(c, text=c)
        tabela.column(c, width=120, anchor="center")
    tabela.pack(fill="both", expand=True)

    
    for item in texto:
        tabela.insert("", "end", values=item)

    tabela.mainloop()

if __name__ == "__main__":
    tabela()


#exibe alertas na tela
def alertas(titulo, mensagem, tipo):
    if tipo == "info":
        messagebox.showinfo(titulo, mensagem)
    elif tipo == "warning":
        messagebox.showwarning(titulo, mensagem)
    elif tipo == "error":
        messagebox.showerror(titulo, mensagem)
    elif tipo == "yesorno":
         resposta = messagebox.askyesno(titulo, mensagem)
         if resposta:
            print("clicou em Sim")
            return True
         else:
            print("clicou em Não")
            return False

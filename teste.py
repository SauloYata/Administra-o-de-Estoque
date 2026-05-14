import tkinter as tk
import sqlite3

# Cria conexão do tkinter com o banco de dados do sqlite
connection = sqlite3.connect("estoque.db")
cursor = connection.cursor()

# Banco de dados da loja 1
cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja1 (nome TEXT, valor TEXT, quantidade INTEGER, vendidos INTEGER)")

cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('Calça', '1990', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('Camisa', '1822', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('Casaco', '2150', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('Vestido', '1599', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('Meias', '999', 11, 9)")

# Banco de dados da loja 2
cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja2 (nome TEXT, valor TEXT, quantidade INTEGER, vendidos INTEGER)")

cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('Calça', '1990', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('Camisa', '1822', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('Casaco', '2150', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('Vestido', '1599', 11, 9)")
cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('Meias', '999', 11, 9)")

# Banco de dados da loja 3
cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja3 (nome TEXT, valor TEXT, quantidade INTEGER, vendidos INTEGER)")

cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('Calça', '1990', 11, 90)")
cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('Camisa', '1822', 11, 59)")
cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('Casaco', '2150', 11, 19)")
cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('Vestido', '1599', 11, 99)")
cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('Meias', '999', 11, 39)")

connection.commit()


def buscar_produto(loja):
    if loja == 1001:
        rows = cursor.execute("SELECT * FROM ProdutosLoja1").fetchall()
        return rows

    elif loja == 2001:
        rows = cursor.execute("SELECT * FROM ProdutosLoja2").fetchall()
        return rows

    elif loja == 3001:
        rows = cursor.execute("SELECT * FROM ProdutosLoja3").fetchall()
        return rows

    else:
        return None


def abrir_tela():
    janela = tk.Tk()
    janela.geometry("300x220")
    janela.title("Estoque da loja")

    tk.Label(janela, text="Administra o estoque", font=("Arial", 14)).pack(pady=10)
    tk.Label(janela, text="Número da loja:").pack(pady=5)

    global entrada_loja
    entrada_loja = tk.Entry(janela, font=("Arial", 12))
    entrada_loja.pack(pady=5)

    tk.Button(janela, text="Ver estoque", width=20, command=login).pack(pady=5)
    tk.Button(janela, text="Sair", width=20, command=janela.destroy).pack(pady=5)

    janela.mainloop()


def login():
    loja = entrada_loja.get().strip()

    if not loja:
        mostrar_msg("digita o número da loja primeiro")
        return

    produtos = buscar_produto(int(loja))

    if produtos is None:
        mostrar_msg("Loja não encontrada")
        return

    texto = ""

    for produto in produtos:
        texto += f"{produto}\n"

    mostrar_msg(texto)


def mostrar_msg(texto):
    estoque = tk.Toplevel()
    estoque.geometry("350x250")
    estoque.title("estoque")

    tk.Label(estoque, text=texto).pack(pady=20)
    tk.Button(estoque, text="ok", command=estoque.destroy).pack()


if __name__ == "__main__":
    abrir_tela()
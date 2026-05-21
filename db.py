import sqlite3
import os

db = "estoque.db"

#cria banco de dados com os produtos no sqlite
def criar_db(path=db):
        if os.path.exists(path):
                print("DB já Existe!")
                return True
        else:
               criar_tabelas()
               print("pegou")

# Conecta o banco de dados do sqlite



def criar_tabelas():        
        # Conecta o banco de dados do sqlite
        connection = sqlite3.connect(f"{db}")
        cursor = connection.cursor()

        # Banco de dados da loja 1
        cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja1 (nome TEXT, valor REAL, quantidade INTEGER, vendidos INTEGER)")

        cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('CALÇA', 19.90, 121, 59)")
        cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('CAMISA', 18.22, 151, 69)")
        cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('CASACO', 21.50, 181, 29)")
        cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('VESTIDO', 15.99, 191, 19)")
        cursor.execute("INSERT INTO ProdutosLoja1 VALUES ('MEIAS', 9.99, 11, 569)")

        # Banco de dados da loja 2
        cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja2 (nome TEXT, valor REAL, quantidade INTEGER, vendidos INTEGER)")

        cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('CALÇA', 18.90, 110, 69)")
        cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('CAMISA', 19.22, 101, 89)")
        cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('CASACO', '7.50', 011, 569)")
        cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('VESTIDO', 12.99, 111, 19)")
        cursor.execute("INSERT INTO ProdutosLoja2 VALUES ('MEIAS', 9.99, 11, 94)")

        # Banco de dados da loja 3
        cursor.execute("CREATE TABLE IF NOT EXISTS ProdutosLoja3 (nome TEXT, valor REAL, quantidade INTEGER, vendidos INTEGER)")

        cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('CALÇA', 39.90, 161, 90)")
        cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('CAMISA', 18.22, 131, 59)")
        cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('CASACO', 22.50, 181, 19)")
        cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('VESTIDO', 13.9, 511, 99)")
        cursor.execute("INSERT INTO ProdutosLoja3 VALUES ('MEIAS', 99.99, 121, 39)")

        connection.commit()
        connection.close()

        print(f"DB {db} criado com sucesso!")

        return True
    


#Lista todos os produtos no estoque de uma loja
def listar_produtos(loja):
    # Conecta o banco de dados do sqlite
    connection = sqlite3.connect(f"{db}")
    cursor = connection.cursor()    
    if loja == 1001:
            produtos = cursor.execute("SELECT * FROM ProdutosLoja1").fetchall()
            return produtos
    
    elif loja == 1002:
            produtos = cursor.execute("SELECT * FROM ProdutosLoja2").fetchall()
            return produtos
    
    elif loja == 1003:
            produtos = cursor.execute("SELECT * FROM ProdutosLoja3").fetchall()
            return produtos
    
    else:
           return "Loja Não Encontrada!"           

#Lista cada produto individualmente no estoque de uma loja
def consultar_produto(nome, loja):
    # Conecta o banco de dados do sqlite
    connection = sqlite3.connect(f"{db}")
    cursor = connection.cursor()    
    if loja == 1001:
            item = cursor.execute(f"SELECT * FROM ProdutosLoja1 WHERE nome = '{nome}'").fetchall()
            if not item:
                  print("Produto não Encontrado!")
                  return False
            
            print(item)
            return item
    
    elif loja == 1002:
            item = cursor.execute(f"SELECT * FROM ProdutosLoja2 WHERE nome = '{nome}'").fetchall()
            print(item)
            return item
    

    elif loja == 1003:
            item = cursor.execute(f"SELECT * FROM ProdutosLoja3 WHERE nome = '{nome}'").fetchall()
            print(item)
            return item

    else:
          return "Loja Não Encontrada" 
    connection.commit()
    connection.close()

def cadastrar_produtos(nome, valor, quantidade, loja):
       
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        if loja == 1001:
            cursor.execute(f"INSERT INTO ProdutosLoja1 (nome, valor, quantidade, vendidos) VALUES (?, ?, ?, ?)", (nome, valor, quantidade, 0))
        
        elif loja == 1002:
             cursor.execute(f"INSERT INTO ProdutosLoja2 (nome, valor, quantidade, vendidos) VALUES (?, ?, ?, ?)", (nome, valor, quantidade, 0))

        elif loja == 1003:
             cursor.execute(f"INSERT INTO ProdutosLoja3 (nome, valor, quantidade, vendidos) VALUES (?, ?, ?, ?)", (nome, valor, quantidade, 0))

        else:
              return "Loja Não Encontrada"
        
        connection.commit()
        connection.close()


import tela
import db

#cria o banco de dados e as tabelas caso não existam
database = "estoque.db"
db.criar_db(database)



if __name__ == "__main__":
    #abre a janela TK
    tela.abrir_tela()
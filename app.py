import tela
import db

#cria o banco de dados e as tabelas caso não existam
db.criar_db()



if __name__ == "__main__":
    #abre a janela TK
    tela.abrir_tela()
import psycopg2

#conn = psycopg2.connect(database="owvendas",user="postgres",password="123", port="5432")
#print("Conexão com o Banco de dados aberta com sucesso!")

#comando = conn.cursor()
#comando.execute(""" CREATE TABLE Agenda
#                (id INT PRIMARY KEY NOT NULL,
#               nome TEXT NOT NULL,
#                telefone CHAR(12))""")
#conn.commit()
#print("Tabela criada  com sucesso no BD!!!")
#conn.close()


class AppBD:
    def __init__(self):
        print("Método Construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="123", host="127.0.0.1", port="5432", database="owvendas")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao Banco de dados", error)

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."PRODUTO"" ("CODIGO", "NOME", "PRECO") VALUES (%s, %s, %s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            #closing database connection
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgreSQL foi fechada.")
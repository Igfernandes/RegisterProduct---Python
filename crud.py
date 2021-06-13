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

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = """Update public."PRODUTO" set "NOME"=%s, "PRECO"=%s where "CODIGO"=%s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro Depois da Atualização")
            sql_select_query = """select * from public."PRODUTO" where "CODIGO"=%s """
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except(Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public."PRODUTO" where "CODIGO"=%s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except(Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:  # closing database connection.
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
import tkinter as tk
import crud as crud


#----------------
# Programa Principal
#---------------

class mainBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        #componentes
        self.lbCodigo = tk.Label(win, text="Nome do produto: ")
        self.lbNome = tk.Label(win, text="Código do Produto:")
        self.lblPreco = tk.Label(win, text="Preço")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text="Cadastrar", command=self.fCadastroProducT)
        self.btnAtualizar = tk.Button(win, text="Atualizar", command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text="Excluir", command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.fLimparTela)

        self.lbCodigo.place(x=100,y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lbNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y =150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

    def flerCampos(self):
        try:
            codigo = self.txtCodigo.get()
            nome = self.txtNome.get()
            preco = self.txtPreco.get()
            print("Leitura dos dados com Sucesso!!")
        except:
            print("Não foi possível ler os dados.")
        return codigo,nome, preco

    def fCadastroProducT(self):
        try:
            codigo, nome, preco = self.flerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.fLimparTela()
            print("Produto Cadastrado com Sucesso!!")
        except:
            print("Não foi possível fazer o cadastro")


    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.flerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            print("Produto Atualizado com Sucesso!")
        except:
            print("Não foi possível fazer a atualização.")

    def fExcluirProduto(self):
        try:
            codigo, nome, preco = self.flerCampos()
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')

    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos Limpos!")
        except:
            print("Não foi possível limpar os campos.")


screen = tk.Tk()
main = mainBD(screen)
screen.title("Bem vindo a Tela de Cadastro")
screen.geometry("600x300")
screen.mainloop()

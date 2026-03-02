class item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo

    def emprestar(self):
        if self.emprestado:
            print("Item já emprestado.")
        else:
            self.emprestado = False
            print("Item emprestado com sucesso.")


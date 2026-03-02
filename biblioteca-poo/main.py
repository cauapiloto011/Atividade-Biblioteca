class itemBiblioteca:
    def __init__(self, codigo, titulo, tema):
        self.codigo = codigo
        self.titulo = titulo
        self.tema = tema

    def cadastrar_livro(self):
        if self.cadastrar_livro:
            print("Livro já cadastrado.")
        else:
            self.cadastrar = False
            print("Livro cadastrado com sucesso.")
        
    def cadastrar_revista(self):
        if self.cadastrar_revista:
            print("Revista já cadastrada.")
        else:
            self.cadastrar = False
            print("Revista cadastrada com sucesso.")

    def listar_itens(self):
        if self.listar_itens:
            print("Nenhum item cadastrado.")
        else:
            self.cadastrar = False
            print("\n--- Lista de Itens ---")
            for item in item:
                print(item)

    def emprestar_Item(self):
        if self.emprestar_Item:
            codigo = input("Digite o código to item para emprestar: ")
            item = buscar_item_por_codigo(itens, codigo)

            if item:
                item.emprestar()
            else:
                print("Item não encontrado.")
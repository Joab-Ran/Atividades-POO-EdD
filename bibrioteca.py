"""A"""

class Pessoa:
    """a"""
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

class Usuario(Pessoa):
    """a"""
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.emprestimos = []

    def _pegar_livro(self, livro):
        if livro.acesso == "Sim":
            if len(self.emprestimos) < 3:
                self.emprestimos.append(livro.titulo)
                print(f"\n{livro.titulo} foi emprestado para {self.nome}")
                livro._acesso_nao()
            else:
                print(f"\nO usuário {self.nome} já tem três livros emprestados")
        else:
            print(f"{livro.titulo} não está disponível para empréstimo")

    def _devolver_livro(self, livro):
        for i in (0,len(self.emprestimos)):
            if self.emprestimos[i] == livro.titulo:
                self.emprestimos.remove(livro.titulo)
                livro._acesso_sim()
                print(f"\n{livro.titulo} foi devolvido")
                break
            else:
                print(f"\n{livro.titulo} não foi emprestado para {self.nome}")
                break

class Administrador(Pessoa):
    """a"""
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.relatorio = []

    def _relatorio(self, item):
        self.relatorio.append(item)

    def _cadastrar_usuario(self, usuario, ida, mt):
        usuario = Usuario(f"{usuario}",f"{ida}",f"{mt}")
        print(f"\nUsuário {usuario.nome} foi cadastrado com sucesso!\n")
        self._relatorio(usuario)
        return usuario

    def _cadastrar_livro(self, livro, au, an, ac):
        livro = Livro(f"{livro}",f"{au}",f"{an}",f"{ac}")
        print(f"{livro.titulo} cadastrado")
        self._relatorio(livro)
        return livro

    def _mostrar_relatorio(self):
        print("\nMostrando Relatório")
        for i in (self.relatorio):
            if i .__class__.__name__ == "Usuario" and len(i.emprestimos) > 0:
                print(f"Usuário: {i.nome}")
                print(f"{i.emprestimos}\n")
            elif i.__class__.__name__ == "Livro" and i.acesso == "Sim":
                print(f"Livro: {i.titulo} está disponível")
        print()

class ItemBiblioteca:
    """a"""
    def __init__(self, titulo, autor, ano, acesso):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.acesso = acesso

class Livro(ItemBiblioteca):
    """a"""
    def __init__(self, titulo, autor, ano, acesso):
        super().__init__(titulo, autor, ano, acesso)

    def _acesso_nao(self):
        self.acesso = "Não"

    def _acesso_sim(self):
        self.acesso = "Sim"

joab = Administrador("Joab",18,210)

guilherme = joab._cadastrar_usuario("Guilherme",19,601)
fabio = joab._cadastrar_usuario("Fábio",20,602)

dracula = joab._cadastrar_livro("Drácula","Bram Stoker","1897","Sim")
frankenstein = joab._cadastrar_livro("Frankenstein","Mary Shelley","1818","Sim")
iliada = joab._cadastrar_livro("A Ilíada","Homero","850-750 a.C","Sim")
odisseia = joab._cadastrar_livro("A Odisséia","Homero","850-750 a.C","Sim")

guilherme._pegar_livro(dracula)
guilherme._pegar_livro(frankenstein)
guilherme._pegar_livro(iliada)
guilherme._pegar_livro(odisseia)

guilherme._devolver_livro(dracula)
guilherme._devolver_livro(dracula)

joab._mostrar_relatorio()

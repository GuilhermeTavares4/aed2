class ListaCircular:
    def __init__(self, max):
        self.max = max
        self.ini = -1
        self.fim = -1
        self.vetor = [None] * max

    def inserir(self):
        pass

    def remover(self):
        pass

    def acessar(self):
        pass

    def exibir_estrutura(self):
        pass

    def buscar_info(self):
        pass

    def acessar_info(self):
        pass

    def tamanho(self):
        if self.fim >= self.ini:
            return self.fim - self.ini + 1
        else:
            return self.max - (self.ini - self.fim) + 1

class ListaLinear:
    def __init__(self, max):
        self.max = max
        self.ini = -1
        self.fim = -1
        self.vetor = [None] * max

    def consultar(self, posicao):
        if self.vazia():
            return None
        if posicao < self.ini or posicao > self.fim:
            return None
        return self.vetor[posicao]
    

    def vazia(self):
        pass

    def tamanho(self):
        tamanho_lista = self.fim + 1 - self.ini
        return tamanho_lista

    def inserir(self, posicao, dado):
        if ((self.ini == 0 and self.fim == self.max - 1) or
        posicao <= 0 or posicao > self.tamanho()+1):
            return False    
        if (self.vazia()):
            self.ini = 0
            self.fim = 0
        elif (self.fim != self.max - 1):
            for i in range(self.fim, self.ini + posicao -2, -1):
                self.vetor[i+1] = self.vetor[i]
            self.fim = self.fim + 1
        else:
            for i in range(self.ini, self.ini + posicao - 1):
                self.vetor[i-1] = self.vetor[i]
            self.ini = self.ini - 1
        self.vetor[self.ini + posicao - 1] = dado

        return True

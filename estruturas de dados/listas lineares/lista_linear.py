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
        for item in self.vetor:
            if item != None:
                return False
        return True

    def tamanho(self):
        tamanho_lista = self.fim + 1 - self.ini
        return tamanho_lista
        
    def inserir(self, dado, posicao):
        if ((self.ini == 0 and self.fim == self.max - 1) or
        posicao < 0 or posicao > self.max - 1):
            print('ao da pra inserir')
            return False
        
        
        if self.vazia():
            self.ini = 0
            self.fim = 0
            
        else:
            right_has_slots = True
            left_has_slots = True

            if self.fim == self.max - 1:
                right_has_slots = False
                go_left = True

            if self.ini == 0:
                left_has_slots = False
                go_left = False

            if right_has_slots and left_has_slots:
                elementos_a_direita = self.fim - posicao
                elementos_a_esquerda = posicao - self.ini
                if elementos_a_esquerda < elementos_a_direita:
                    go_left = True
                else:
                    go_left = False
            print(go_left)


            if go_left:
                for i in range(self.ini, posicao - 1):
                    self.vetor[i - 1] = self.vetor[i]
                self.ini = self.ini - 1
            else:
                for i in range(self.fim + 1, posicao, -1):
                    self.vetor[i] = self.vetor[i - 1]
                self.fim = self.fim + 1

        self.vetor[self.ini + posicao] = dado




            

        return True

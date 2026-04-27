
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo_nodo: Nodo = None
        

class ListaEncadeada:
    def __init__(self):
        self.ini: Nodo = None
        self.tamanho = 0

    def adicionar_nodo(self, nodo: Nodo, pos: int):
        if pos <= 0 or pos > self.tamanho + 1:
            print('posicao errada')
            return False
        
        if pos == 1:
            prox = self.ini
            self.ini = nodo
            self.ini.proximo_nodo = prox
            print('nodo inserido no inicio')

        elif pos == self.tamanho + 1:
            ultimo_nodo = self.pegar_nodo(self.tamanho)
            ultimo_nodo.proximo_nodo = nodo
            print('nodo inserido no final')

        else:
            nodo_temp = self.pegar_nodo(pos)
            nodo_anterior = self.pegar_nodo(pos - 1)
            
            nodo_anterior.proximo_nodo = nodo
            nodo.proximo_nodo = nodo_temp

        self.tamanho += 1
        
    def pegar_nodo(self, pos: int):
        if self.tamanho == 0:
            return None
        
        nodo = self.ini
        for i in range(pos - 1):
            nodo = nodo.proximo_nodo

        return nodo

    def printa_nodos(self):
        nodo = self.ini
        for i in range(self.tamanho):
            print(f'nodo {i + 1}: {nodo.valor}')
            nodo = nodo.proximo_nodo





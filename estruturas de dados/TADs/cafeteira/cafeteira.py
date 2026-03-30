import time

class Cafeteira:
    def __init__(self, cap_max_agua, cap_max_cafe):
        self.cap_max_agua = cap_max_agua
        self.cap_max_cafe = cap_max_cafe
        self.nivel_agua = 0
        self.nivel_cafe = 0
        self.acesa = False

    def ligar(self):
        self.acesa = True

    def desligar(self):
        self.acesa = False

    def abastecer_agua(self, ml):
        novo_nivel = self.nivel_agua + ml
        if novo_nivel > self.cap_max_agua:
            print(f'boa derramou {novo_nivel - self.cap_max_agua} mls de água nessa merda')
            self.nivel_agua = self.cap_max_agua
        else:
            self.nivel_agua = novo_nivel
        
    def ver_status(self):
        estado = 'ligada' if self.acesa else 'desligada'
        print(f"A cafeteira está {estado}, seu nível de água está em {self.nivel_agua} mls, seu nível de café está em {self.nivel_cafe} mgs.")

    def abastecer_cafe(self, mg):
        novo_nivel = self.nivel_cafe + mg
        if novo_nivel > self.cap_max_cafe:
            print(f'Desperdiçou {novo_nivel - self.cap_max_cafe} mgs de café né, mas tudo bem !!!')
            self.nivel_cafe = self.cap_max_cafe
        else:
            self.nivel_cafe = novo_nivel
    
    def fazer_cafe(self):
        if not self.acesa:
            print('Liga a cafeteira primeiro')
            return
        if self.nivel_cafe <= 10 or self.nivel_agua <= 100:
            print('po faz um cafe decente ai namoral')
            return
        self.nivel_agua -= 100
        self.nivel_cafe -= 10
        print('Fazendo café...')
        time.sleep(2)
        print('Café pronto!')



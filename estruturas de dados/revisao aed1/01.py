# Faça um programa em Python que construa uma lista
# com n inteiros. Após, mostre o menor e o maior valor
# presente na lista. ( sem usar Min ou Max)

lista = []
tamanho_lista = int(input('Digite o tamanho da lista: '))

for i in range(tamanho_lista):
    num = int(input('digite um numero: '))
    lista.append(num)

menor = 0
maior = 0

for num in lista:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f'Menor: {menor}. Maior: {maior}')

# Faça um programa que construa uma lista com tamanho
# e elementos informados pelo usuário. Após construída,
# solicitar que o usuário informe um valor a ser buscado na
# lista. Se o valor estiver na lista, informar a sua posição;
# senão, informar que não existe na lista (valor “False”).


lista = []
tamanho_lista = int(input('Digite o tamanho da lista: '))

for i in range(tamanho_lista):
    valor = input('digite um numero: ')
    lista.append(valor)

valor_buscado = input('Digite um valor para ser encontrado na lista: ')

posicoes_do_valor = []

for i, item in enumerate(lista):
    if valor_buscado == item:
        posicoes_do_valor.append(str(i))

if len(posicoes_do_valor) == 0:
    print('O valor não foi encontrado.')
else:

    posicoes_string = ', '.join(posicoes_do_valor)
    posicoes_string = ' e'.join(posicoes_string.rsplit(',', 1))
    print(f'O valor digitado foi encontrado nas posições {posicoes_string}.')
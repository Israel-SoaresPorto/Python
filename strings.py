nome = 'israel'

tamanho_nome = len(nome)
nova_string = ''
indice = 0

while indice < tamanho_nome:
    if indice == (tamanho_nome - 1):
        nova_string += nome[indice]
        break
    else:
        nova_string += (nome[indice] + '*')

    indice += 1

print(nova_string)

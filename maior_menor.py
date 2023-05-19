"""
    pede para inserir três números inteiros e exibir o maior e o menor 
    número entre eles.

"""

numeros = []  # lista de números inteiros

# entrada de dados para a lista
for i in range(1, 4):
    numero = int(input(f'digite o {i}° número: '))
    numeros.append(numero)


maior = numeros[0]  # variavel para maior número
menor = numeros[0]  # variavel para menor número

# pecorrendo a lista para verificar o maior e o menor número da lista
for i in numeros:
    if i > maior:
        maior = i

    if i < menor:
        menor = i


print(f"maior número: {maior}")  # exibe o maior número
print(f'menor número: {menor}')  # exibe o menor número

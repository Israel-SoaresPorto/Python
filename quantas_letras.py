# variável para uma frase qualquer(pode ser modificada)
frase = "Python é uma linguagem de programação multiparagdima. " \
    "Python foi criado por Guido Van Rossum".lower()

qtd_de_vezes_que_apareceu = 0
letras_que_apareceram_mais_vezes = []

"""
iterando a frase para descobrir oa maior quandidade de letras que aparece
na frase.
"""
for i in range(len(frase)):
    letra_atual = frase[i]  # pega a letra atual da interação
    # descobre a quantidade de vezes que a letra aparece na frase
    quantas_vezes = frase.count(letra_atual)

    # condição para ignorar espaços em brancos
    if letra_atual == ' ':
        continue

    # armazena o valor da letra de maior incidência na frase
    if quantas_vezes > qtd_de_vezes_que_apareceu:
        qtd_de_vezes_que_apareceu = quantas_vezes


"""
iterando a frase para verificar as letras com maior quantidade na frase
"""
for j in range(len(frase)):
    letra_atual = frase[j]
    quantas_vezes = frase.count(letra_atual)

    if letra_atual == ' ':
        continue

    # armazenas as letras que aparecem com maior quantidade na frase
    if quantas_vezes == qtd_de_vezes_que_apareceu:
        # evita que a mesma letra seja armazenada na lista
        if letra_atual not in letras_que_apareceram_mais_vezes:
            letras_que_apareceram_mais_vezes.append(letra_atual)

print(f'frase: {frase}')  # exibe a frase
print(f'letras que apareceram mais vezes: {letras_que_apareceram_mais_vezes}')
print(f'quantidade de vezes que apareceu: {qtd_de_vezes_que_apareceu}')

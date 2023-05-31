from random import choice as rand

listas_palavras = ['banana', 'morango', 'acerola', 'laranja', 'tangerina',
                   'goiaba']

palavra_secreta = rand(listas_palavras)

lista_palavra_secreta = ["_" for i in range(len(palavra_secreta))]

tentativas = 5

print("BEM-VINDO AO JOGO DA FORCA")
print(f'VOÇÊ TÊM {tentativas} TENTATIVAS PARA DESCOBRIR A PALAVRA SECRETA')
print('DIGITE UMA LETRA QUE POSSA ESTAR NA PALAVRA SECRETA')
print('CADA ERRO CONSUME UMA TENTATIVA; SE ACERTAR, NÃO CONSOME TENTATIVA')
print('SE NÃO CONSEGUIR ACERTAR A PALAVRA ATÉ ACABAR AS TENTATIVAS, GAMER OVER.')
print('BOA SORTE E DIRVITA-SE!')


while tentativas > 0:

    print(f'TENTATIVAS: {tentativas}')
    letra = input('digite uma letra: ')

    if letra in palavra_secreta:
        print('voçê descobriu uma letra da palavra secreta.')

        for l in range(len(palavra_secreta)):
            if letra in palavra_secreta[l]:
                lista_palavra_secreta[l] = letra
    else:
        print('ops, voçê errou!')
        tentativas -= 1

    print(lista_palavra_secreta)

    if "_" not in lista_palavra_secreta:
        print(f'PARABENS, VOÇÊ ADIVINHOU A PALAVRA SECRETA: {palavra_secreta}')
        break

    if tentativas == 0:
        print('QUE PENA, SUAS TENTATIVAS ACABARAM E VOÇÊ NÃO DESCOBRIU A' +
              f'PALAVRA SECRETA: {palavra_secreta}')

print('FIM DE JOGO.')

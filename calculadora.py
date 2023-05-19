# calculadora em Python

# loop iniciador do programa
while True:
    try:
        # entrada de dado do primeiro número
        numero_1 = float(input('digite o primeiro número: '))
        # entrada de dado do segundo número
        numero_2 = float(input('digite o segundo número: '))

        """
        entrada de dado da operação a ser feita
        - caracteres de operações:
          + : adição, 
          - : subtração
          * : multiplicação
          / : divisão
        """
        operador = input('digite um sinal de operação(+, -, *, /): ')

        # realiza a operação a partir da opreraçaõ digitada
        if operador == '+':
            resultado = numero_1 + numero_2
            print(f"resultado da adição: {resultado}")
        elif operador == '-':
            resultado = numero_1 - numero_2
            print(f"resultado da subtração: {resultado}")
        elif operador == '*':
            resultado = numero_1 * numero_2
            print(f"resultado da multiplicação: {resultado}")
        elif operador == '/':
            resultado = numero_1 / numero_2
            print(f"resultado da divisão: {resultado}")
        else:
            # exibe uma mensagen caso seja digitado um valor de operação valido
            print('operador incorreto, operação não ralizada.')
    except ValueError:
        # lança uma exceção de tipo do input
        print('valor digitado não é um número.')
    except ZeroDivisionError:
        # lança uma exceção de divisão por zero
        print("não é possivel dividir por zero.")

    # variável booleana para interronper o laço
    sair = input('deseja sair da calculadora?(s/n): ').lower().startswith('s')

    if sair:
        break

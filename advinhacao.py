def jogar():  #é a função main (do C), só que o Python não precisa que eu faça obrigarotiamente igual no C, posso usar ela normalmente sem fazer.
    import random
    #JOGO
    print('*************************************')
    print('Seja bem vindo ao jogo de advinhacao!')
    print('*************************************')
    numero_secreto = random.randrange(0, 101)#numero entre 0 e 100
    total_de_tentativas = 3

    #variaveis
    total_de_tentativas = 0
    rodada = 0
    pontos = 1000

    print("**-- Defina o nível -- **")
    print("** (1) - Fácil         **")
    print("** (2) - Médio         **")
    print("** (3) - Díficil       **")
    print("-------------------------")
    nivel = int(input("Defina: "))

    if (nivel == 1):
        total_de_tentativas = 20

    elif (nivel == 2):
        total_de_tentativas = 10

    elif (nivel == 3):
        total_de_tentativas = 5

    #for rodada in range(1 (comeco), 10(fim), 1(soma de 1 em 1)):
        # a funcao range tem o seguinte esquema: range(start, stop, [step])
    for rodade in range(1, total_de_tentativas + 1):
        print("\n")
        rodada += 1
        print(f'Tentativa {rodada} de {total_de_tentativas}') #usar o .format para numeros
        chute = int(input('Digite um número entre 1 e 100: '))
        print(f'Você digitou: {chute}')

        if(chute < 1 or chute > 100):
            print("Você digitou um número inválido, tente novamente!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou): #testa a igualdade = acerto
            print(f'Voce acertou e fez {pontos:.2f} pontos!')
            break
        else:
            if (maior): #testa valor acima
                print("Você errou! O seu chute foi maior que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)  # abs = funcao absoluta, pra pegar o numero independente do sinal
                pontos = pontos - pontos_perdidos
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. E você fez {pontos} pontos")
            elif (menor): #testa valor abaixo -- elif: else if
                print("Você errou! O seu chute foi menor que o numero secreto")
                pontos_perdidos = abs((numero_secreto - chute) / 3) #abs = funcao absoluta, pra pegar o numero independente do sinal
                pontos = round(pontos - pontos_perdidos)
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. E você fez {pontos} pontos")

    print("Fim do jogo.")
if(__name__ == "__main__"): #função que possibilita jogar esse jogo diretamente e não somente atraves do jogos
    jogar()
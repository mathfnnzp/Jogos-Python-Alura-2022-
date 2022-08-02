import random

def jogar():  #def = função

    imprimir_menu()
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto (~F v ~F = V v V = V)
    while (not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra_secreta):
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f'Ops, você errou! Você possui {7-erros} tentativas.')
            desenhar_forca(erros)

        enforcou = erros == 7 #7 tentativas
        acertou= '_' not in letras_acertadas
        print(letras_acertadas)



    if (acertou):
        imprimir_mensagem_vencedor()
    else:
       imprimir_mensagem_perdedor(palavra_secreta)

    print('Fim do jogo!')


def imprimir_menu():
    print('********************************')
    print('Seja bem vindo ao jogo da Forca!')
    print('********************************')
    print('Obs: não utilize acentuações e ç')

def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    with open("palavras.txt") as arquivo:  # função para fechar o arquivo mesmo quando der erro
        for linha in arquivo:
            linha = linha.strip()  # tira o /n da palavra que já vem padrão no txt
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))  # gera o número aleatorio da palavra selecionada - ex: 0 = maça
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

    # LIST COMPREHENSIONS: também permite utilizar condições para o preenchimento da lista.
    # inteiros = [1,3,4,5,7,8,9]
    # pares = [x for x in inteiros if x % 2 == 0]

    # código acima printa somente os números pares

def inicializa_letras_acertadas(ps):
    return ['_' for letra in ps]
    # NOME DA FUNCIONALIDADE: LIST COMPREHENSIONS
    #ps = palavra secreta

def pedir_chute():
    chute = str(input('Digite uma letra: '))
    chute = chute.strip().upper()  # strip = função para ignorar os espaços
    return chute

def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    #c = chute, lc= letras_acertadas, pls= palavra_secreta
    index = 0  # variável parar guardar posição da letra encontrada
    for letra in palavra_secreta:
        if (chute == letra):  # deixo tudo em maiúsculo para evitar erros
            # print(f'Encontrei a letra {letra} na posição {index}') - foi substituído pela linha abaixo
            letras_acertadas[index] = letra  # se acertar = vou sobreescrever "_" pela letra acertada
        index += 1  # caso acertado, ele guarda

def imprimir_mensagem_vencedor():
    print('Parabéns! Você ganhou!')

def imprimir_mensagem_perdedor(plsc):
    print(f'A palavra secreta era {plsc}!')
    print('Infelizmente, você perdeu! Jogue novamente.')


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'): #função que possibilita jogar esse jogo diretamente e não somente atraves do jogos
    jogar()
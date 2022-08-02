import forca
import advinhacao

def escolhe_o_jogo():
    print('*****************************************')
    print('Seja bem vindo ao menu de jogos         !')
    print('*****************************************')
    print('Escolha seu jogo (1) advinhação (2) forca')
    jogo = int(input('Defina: '))

    if (jogo == 1):
        print('Jogando advinhação')
        advinhacao.jogar() #funcao
    elif (jogo == 2):
        print('Jogando forca')
        forca.jogar() #funcao

if(__name__ == "__main__"): #função que possibilita jogar esse jogo diretamente e não somente atraves do jogos
    escolhe_o_jogo()

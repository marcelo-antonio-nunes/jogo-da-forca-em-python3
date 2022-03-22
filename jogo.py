import random
import os
import platform


def limpa_termial() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Linux":
        os.system("clear")
    logo_do_jogo()


def carrega_lista(arquivo: str) -> list[str]:
    ''' BUSCA NO ARQUIVO APONTADO AS PALAVRAS,
    E RETORNA UM NOVA LISTA COM AS PALAVRAS '''
    nova_lista: list[str] = []
    with open(arquivo, 'r') as f:
        texto = f.readlines()
        for texto in texto:
            nova_lista.append(texto.strip())
    return nova_lista


def carrega_palavra_da_lista(lista: str) -> str:
    ''' CARREGA UMA PALAVRA ALIATORIAMENTE
    DA LISTA APONTADA E RETORNA A PALAVRA '''
    return random.choice(lista)


def logo_do_jogo() -> None:
    ''' MOSTRA O NOME DO JOGO '''
    print('==================')
    print('= Jogo da forca! =')
    print('==================\n')


def armazena_os_palpites(palpite: str, palavra_secreta: str) -> set[str]:
    certo: bool = False
    '''RECEBE O PALPITE E ARMAZENA EM UM SET, LISTA NÃO
       ORDENADA, SEM ITEMS REPETIDOS'''
    if palpite in palavra_secreta:
        certo = True
        return palpite, certo
    else:
        certo = False
        return '', certo


def checa_palpite_e_chances(palpites: set[str], palavra_secreta: str) -> str:
    ''' CHECA SE PALPITE ESTA CONTIDO NA PALAVRA SECRETA '''
    saida: str = ""
    for letra in palavra_secreta:
        if letra in palpites:
            saida += letra
        else:
            saida += '_'
    return saida


def inprime_derrota(resposta: str) -> None:
    limpa_termial()
    print('INFELISMENTE VOCÊ PERDEU :(')
    print(f'A resposta correta é {resposta.upper()}\n')
    input()
    exit()


def imprime_vitoria(resposta: str) -> None:
    print(f'A resposta correta é {resposta.upper()}\n')
    print('Você GANHOUUUUU!!!')
    input()
    exit()

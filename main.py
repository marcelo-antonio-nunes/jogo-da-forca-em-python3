from jogo import *


# FUNÇÃO PRINCIPAL #
def main() -> None:
    limpa_termial()
    chances: int = 6
    palpites: set[str] = {''}
    nova_lista: list[str] = carrega_lista('palavras.txt')
    palavra: str = carrega_palavra_da_lista(nova_lista)
    while True:
        # CRIA UMA LISTA COM OS PALPITES RECEBIDO SEM REPETIR E
        # RETORNA UM BOOLEANO CERTO = False OU TRUE PARA CONTROLAR
        # AS CHANCES
        palpite, certo = (armazena_os_palpites(
            input('Digite seu palpite: '), palavra))
        palpites.add(palpite)
        # DECREMENTA AS CHANCES CASO O PALPITE NÃO ESTEJA CERTO
        chances -= 1 if not certo else 0
        # SE ESGOTAREM AS CHANCES IMPRIME A MENSAGEM DE DERROTA
        if chances == 0:
            inprime_derrota(palavra)
        # CHECA SE TEM ALGUM DOS PALPITES CONTIDO NA PALAVRA SECRETA
        # SE TIVER É ACRECENTADO A VARIAVEL SAIDA
        # CASO ACERTE TODAS AS LETRAS DA PALAVRA, IMPRIME MENSAGEM
        # DE VITORIA AO GANHADOR !
        saida = checa_palpite_e_chances(palpites, palavra)
        if saida == palavra:
            limpa_termial()
            imprime_vitoria(palavra)
        limpa_termial()
        # IMPRIME AS CHANCES QUE RESTAM
        print(f' Você tem {chances} chance\n')
        print(saida, end='\n\n')


if __name__ == '__main__':
    main()

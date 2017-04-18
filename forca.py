"""Fonte do curso de python alura"""

def forca():
    """ Jogo de forca """
    print(38 * "*")
    print(5  * "*", 'Bem Vindo ao Jogo da Força', 5 * '*')
    print(38 * '*')

    palavar_secreta = 'banana'
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input('Qual é a letra? ')

        index = 0
        for letra in palavar_secreta:
            if (chute.upper() == letra.upper()):
                print(f'Encontrei a letra {letra} na posição {index}')
            index = index + 1

    print("Fim do jogo")

if __name__ == '__main__':
    forca()

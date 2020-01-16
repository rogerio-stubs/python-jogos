def jogar():
    print('*************************************')
    print('*****Bem vindo ao jogo da Forca!*****')
    print('*************************************')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input('Qual letra? ').lower().strip()
        print('chute', chute)
        
        # finalizando jogo
        if (chute == 'fim'):
            enforcou = acertou = True

        
        index = 0
        for letra in palavra_secreta:
            if (letra == chute):
                print('Encontrei a letra {} na posição {}.'.format(letra, index))
            index += 1

        print('Jogando...')

    print('Fim de jogo')

if (__name__ == '__main__'):
    jogar()

def jogar():
    print('*************************************')
    print('*****Bem vindo ao jogo da Forca!*****')
    print('*************************************')

    palavra_secreta = 'banana'
    letras_acertadas = list(['_' for x in range(len(palavra_secreta))])

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print('Forca {}'.format(letras_acertadas))
        chute = input('Qual letra? ').lower().strip()
        print('chute', chute)
        
        # finalizando jogo
        if (chute == 'fim'):
            enforcou = acertou = True

        
        index = 0
        for letra in palavra_secreta:
            if (letra == chute):
                print('Encontrei a letra {} na posição {}.'.format(letra, index))
                letras_acertadas[index] = letra
            index += 1

        print('Jogando...')

    print('Fim de jogo')

if (__name__ == '__main__'):
    jogar()

def jogar():
    print('*************************************')
    print('*****Bem vindo ao jogo da Forca!*****')
    print('*************************************')

    palavra_secreta = 'banana'
    letras_acertadas = list(['_' for x in range(len(palavra_secreta))])

    acertou = False
    erros = 0
    quantidade_tentativas = 6

    while (not acertou):
        print('Forca {}'.format(letras_acertadas))
        chute = input('Qual letra? ').lower().strip()

        if (chute not in palavra_secreta):
            erros += 1
            if (erros == quantidade_tentativas):
                print('Você perdeu!!!')
                break

        index = 0
        for letra in palavra_secreta:
            if (letra == chute):
                letras_acertadas[index] = letra
            index += 1

        print('\n')

        acertou = '_' not in letras_acertadas
        if (acertou):
            print('Parabéns você acertou a palavra secreta')

if (__name__ == '__main__'):
    jogar()

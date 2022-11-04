import os
def jogo_forca():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("********************************\n")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
    print("**************")
    print("Fim de Game!!")
    print("\n" * os.get_terminal_size().lines)
    print("**************")

if(__name__ == "__main__"):
    jogo_forca()
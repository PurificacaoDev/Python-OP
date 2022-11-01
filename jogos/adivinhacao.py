#Feito para rodar um jogo de adivinhacao em python #
import random

def jogo_adivinhacao():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")
    numero__secreto = random.randrange(1, 101)
    chances = 0
    contador = 1
    pontuação = 1000
    pontos_perdidos = 0
    print("Qual o nivel de Dificuldae?")
    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input("Defina a dificuldade"))

    if(nivel == 1):
        chances = 20
    elif(nivel == 2):
        chances = 10
    else:
        chances = 5


    for contador in range(1, chances + 1):
        print("********************************")
        print("Voce esta na chance {} de {}".format(contador, chances))
        chute = int(input("Digite o seu chute entre 1 e 100: ",))
        print("********************************")
        print("Voce digitou, ", chute)
        if(chute < 1 or chute > 100):
            print("Voce perdeu uma chance, digite um numero valido entre 1 e 100")
            continue
        acertou = chute == numero__secreto
        maior = chute > numero__secreto
        menor = chute < numero__secreto
        if(acertou):
            print("Voce acertou  e sua pontuação foi {}".format(pontuação))
            break
        else:
            print("Voce errou!!")
            if(maior):
                print("Seu chute foi acima do numero\n")
                pontos_perdidos = abs(chute - numero__secreto)
                pontuação = pontuação - pontos_perdidos
            elif(menor):
                print("Seu chute foi abaixo do numero\n")
                pontos_perdidos = abs(numero__secreto - chute)
                pontuação = pontuação - pontos_perdidos

    print("Fim de jogo!!!")
    print("Sua pontuação final foi",pontuação)

if(__name__ == "__main__"):
    jogo_adivinhacao()


 #Exemplo de For usando Step
 #for contado in range (1[Inicia],11[Finaliza],3[salta de 3 em 3])
#Feito para rodar um jogo de adivinhacao em python #
import random
print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")
numero__secreto = random.randrange(1, 101)

print(numero__secreto)

chances = 3
contador = 1

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
        print("Voce acertou, a resposta pra tudo é", numero__secreto)
        break
    else:
        print("Voce errou!!")
        if(maior):
            print("Seu chute foi acima do numero\n")
        elif(menor):
            print("Seu chute foi abaixo do numero\n")

print("Fim de jogo!!!")

 #Exemplo de For usando Step
 #for contado in range (1[Inicia],11[Finaliza],3[salta de 3 em 3])
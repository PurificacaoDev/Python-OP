#Feito para rodar um jogo de adivinhacao em python #
print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")
numero__secreto = 42
chances = 3
contador = 0
while contador < chances:
    chute = int(input("Digite o seu chute: "))
    print("Voce digitou, ", chute)
    acertou = chute == numero__secreto
    maior = chute > numero__secreto
    menor = chute < numero__secreto
    if(acertou):
        print("Voce acertou, a resposta pra tudo é",numero__secreto)
        contador = 5
    else:
        print("Voce errou!!")
        if(maior):
            print("Seu chute foi acima do numero\n")
        elif(menor):
            print("Seu chute foi abaixo do numero\n")
        contador = contador +1

print("Final!!!")
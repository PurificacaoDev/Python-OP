import forca
import adivinhacao

print("********************************")
print("Escolha o jogo que deseja começar")
print("********************************")

print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual o Jogo? "))

if(jogo == 1):
    print("Jogo Forca")
    forca.jogo_forca()
elif(jogo == 2):
    print("Jogo Adivinhação")
    adivinhacao.jogo_adivinhacao()
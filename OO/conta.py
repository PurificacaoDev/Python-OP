

class Conta:
    #Cria uma conta com seus atributos
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo o Objeto")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #Imprimi o saldo atual da conta
    def extrato(self):
        print("{} seu saldo é de R${}".format(self.titular,self.saldo))

    #Efetua um depoisito na conta criada anteriormente
    def depositar(self,valor):
        self.saldo += valor

    #Saca um valor na conta criada anteriormente
    def sacar(self,valor):
        self.saldo -= valor
        
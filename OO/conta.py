

class Conta:
    #Cria uma conta com seus atributos
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo o Objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Imprimi o saldo atual da conta
    def extrato(self):
        print("{} seu saldo é de R${}".format(self.__titular,self.saldo))

    #Efetua um depoisito na conta criada anteriormente
    def depositar(self,valor):
        self.__saldo += valor

    #Saca um valor na conta criada anteriormente
    def sacar(self,valor):
        self.__saldo -= valor
    def transfere(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

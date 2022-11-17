

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
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    #Get sempre pega e e "imprime" o valor
    @property
    def limite(self):
        return self.__limite
    #Set sempre pega e altera o valor ou o atributo
    @limite.setter
    def limite(self, limite):
        self.__limite = limite


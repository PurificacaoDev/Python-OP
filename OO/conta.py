

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


    #Verifica a disponibilidade de valores a sacar
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    #Saca um valor na conta criada anteriormente
    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Voce passou do limite de saque")

    def transfere(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    #Get sempre pega e e "imprime" o valor
    @property
    def limite(self):
        return self.__limite

    #Set sempre pega e altera o valor ou o atributo
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigo_banco(self):
        return "001"

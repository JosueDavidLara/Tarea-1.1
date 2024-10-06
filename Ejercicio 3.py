class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito: float):
        if deposito > 0:
            self.saldo += deposito
            print("Deposito finalizado con éxito")
            print(f"Su nuevo saldo es de: {self.saldo}")
        else:
            print("No puede depositar negativo asdkjlsanfkjnsakjf")

    def retirar(self, retiro: float):
        if retiro <= self.saldo:
            self.saldo -= retiro
            print("Retiro finalizado con éxito")
            print(f"Su nuevo saldo es de: {self.saldo}")
        else:
            print("No puede retirar mas de lo que hay asdkjlsanfkjnsakjf")

    def mostrar_saldo(self):
        print(f"Su saldo es de: {self.saldo}")


cuenta = CuentaBancaria(titular="Suplente")

cuenta.depositar(1000)
cuenta.retirar(500)
cuenta.retirar(700)
cuenta.depositar(-100)
cuenta.mostrar_saldo()

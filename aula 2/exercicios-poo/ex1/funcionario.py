from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, first_name, last_name, address, phone, email, salary, position):
        super().__init__(first_name, last_name, address, phone, email)
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"Funcionario: {self.first_name}, salário {self.salary} e posição {self.position}"        
from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, first_name, last_name, address, phone, email, gender, socialnetwork):
        super().__init__(first_name, last_name, address, phone, email)
        self.gender = gender
        self.socialnetwork = socialnetwork

    def __str__(self):
        return f"Client: {self.first_name} {self.last_name} - {self.gender}"
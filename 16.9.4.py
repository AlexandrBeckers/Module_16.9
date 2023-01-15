class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}. {self.city}. Баланс:{self.balance} руб."'

    def corporate_list(self):
        return f'{self.name} {self.surname}, г. {self.city}'

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Сергей", "Бурунов", "Москва", 129)

guests = [client_1, client_2]

for guest in guests:
    print(guest.corporate_list())
class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Customer name is {self.name} and age is {self.age}")
    def party(self):
        print(f"Party name is {self.name} and age is {self.age}")
customer1 = Customer(name = "Rojay", age= 25)
party = Customer(name="ram", age= 64)
customer1.display()
party.party()
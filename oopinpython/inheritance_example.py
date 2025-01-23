#inheritance in python 
# it allow a class to inherit attributes and methods from another class it promotes the code reuasbitity and make it easier to maintain and read code

#Example inheritance (single inheritance )
class ParentClass:
    def method_in_parent(self):
        print( "parent class method")
#derive class
class ChildClass(ParentClass):
    def method_in_childclass(self):
        print("this is a method is in child class")

#example usese creating object
child = ChildClass()
parent = ParentClass()
parent.method_in_parent()
child.method_in_parent()
child.method_in_childclass()

#create a program using inheritance feature where user loging in a system with diffrent types : admin, normal user, customer 
      #example of hierarchical inherritance
#creating class 
class User:
    def __init__(self, username,email, password):
        self.username = username
        self.email= email
        self.password = password
    def login(self):
        return f"{self.username} logged in."
    def update_profile(self, new_email):
        self.email= new_email
        return f"{self.username} is updated with {self.email}"

#Child class
class Admin(User):
    def mange_user(self):
        return f"{self.username} is mange by user"

class Product(User):
    def add_product(self, product_name):
        self.product_name = product_name
        return f"{self.username} added a product {product_name}"

class Customer(User):
    def purchase(self, product_name):
        self.product_name = product_name
        return f"{self.username} pruchase a product {product_name}"

# creating objects 
admin = Admin ("admin123", "ad@gmail.com", "pass123")
product =Product("Ram", "ram@gmail.com", "pass123")
customer = Customer('customer', "ustomer@cu.com", "pass123")

#accessing classs
print(admin.login()) 
print(admin.mange_user())

print(product.login())
print(product.add_product("mobile"))

print(customer.login())
print(customer.purchase("mobile"))
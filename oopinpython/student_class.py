# solve problems by creating object
# benifit : 1. increase reusability and decress complexicity 2. easier for debug and modify and reduce code repitation

#class : class is a blue print for creating a object and it define the properity and methods that an object will have. 
# EXAMPLE:  a CLASS called DOG might have property like breed color and METHOD like bark, run 
#### method are like task or operaton of class.
#............... medthod are function define inside a class that describe the behaviour of the object 

#creating first class 
class student:
    def __init__(self, name, age, grade):
        #attributes: student's name, age, grade
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name is : {self.name}, Age: {self.age}, Grade: {self.grade}"
    def is_passing(self):
        #method : checks if the student is passing 
        return self.grade >= 60

# creating student object
st1 = student("rojay", 25, 80)
st2 = student("roshan", 30, 79.5)

#accessing the student details
print(st1.get_details())
print(st2.get_details())

#checking if the student is passing or not 
print(f"Student one is passed: {st1.is_passing()}")
print(f"student two is passed: {st2.is_passing()}")

# write a program to create a class laptop with the porperty id name and ram. Then create three objects of this class all their details 

class Laptop:
    def __init__(self, id, brand_name, model, ram_storage, graphic_card, price):
        self.id = id
        self.brand_name = brand_name
        self.model = model
        self.ram_storage = ram_storage
        self.graphic_card = graphic_card
        self.price= price

    def get_details(self):
       return (
        F"{self.brand_name}s laptop with {self.model} model number having ram storage {self.ram_storage} and {self.graphic_card} graphic"
        F"has lunched in market in ID {self.id} at price {self.price}"
        )

#creating objects 
laptop1= Laptop( "1", "acre nitro", "n3456hr3", "16GB", "6GB", "119999")

#accessing the laptop details
print(laptop1.get_details())



#Basic example of inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        return f"Name: {self.name} and Age: {self.age}"

class Student(Person):
    def __init__(self, name, age,grade):
        #Call the constructor of the base class 
        super().__init__(name, age)
        self.grade = grade

    def is_passing(self):
        return self.grade >=60

#Creating the objects using student calss 
student = Student("Ram", 70, 69)
#Access inheritance and new attribute and method 
print(student.get_details())
print(f"Is the student Passing? {student.is_passing()}")


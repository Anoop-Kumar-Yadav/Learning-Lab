'''
Instance variable : copy for different object but value is different for each one.
                    modification in it not reflect in other objects

WAYS OF CREATION :
    1. Using Constructor
    2. Using instance method
    3. outside class
'''

class Employee:
    def __init__(self,name,salary):
        self.name = name # instance variable
        self.salary = salary # instance variable
    
    def display(self):
        self.new_inst_var = "Nothing"
        
    def display_2(self):
        print(self.new_inst_var)

e1 = Employee("Akshay",5000)
e2 = Employee("Amit",7000)
e3 = Employee("Aditya",4000)

#------------------------------------------------------
# Outside Class

e1.age = 21 # instance variable creation outside class

print(hasattr(e1,"age")) #True
print(hasattr(e2,"age")) #False

del e1.age # deletion of instance varibale 
print(hasattr(e1,"age")) #False

e1.display() # instance variable creation in method
print(hasattr(e1,"new_inst_var")) #True
print(hasattr(e2,"new_inst_var")) #False

e1.display_2() # Nothing


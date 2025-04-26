'''
Class Varible :
    > made for entire class (All Objects)
    > only one copy is creted and districuted to all objects
    > modifiction (using class reference) in class variable reflect in all object 
'''

class Employee:
    Company_name = "TCS" # class variable

    def __init__(self,name,salary):
        self.name = name # instance variable
        self.salary = salary # instance variable
    
    #>> Modification using class method
    @classmethod
    def display(cls):
        return (cls.Company_name)
    
    @classmethod
    def modify(cls):
        cls.Company_name = "Google"

e1 = Employee("Akshay",5000)
e2 = Employee("Amit",7000)

'''Access class variable outside the class'''
#----------------------------------------------
#>> using class reference
print(Employee.Company_name) # TCS

#>> using object refernce
print(e1.Company_name) # TCS

#>> using class method
print(Employee.display()) # TCS

'''Modification class variable outside the class'''
#----------------------------------------------
#>> can be done only using class reference
Employee.Company_name = "Infosys"
print(Employee.Company_name) # Infosys

#>> modifiction using class method
Employee.modify()
print(Employee.display()) # Google

#>> but if try modification using object it create new instance varibale for that object
e1.Company_name = "TATA"
print(Employee.Company_name) # Google
print(e1.Company_name) # TATA


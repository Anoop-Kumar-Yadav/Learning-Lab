# In Python Everything is object of some class

x = 10

# To check class of object
print(type(x))  # <class 'int'>


# Class are 2 Types : Built-In , user Define 

# Syntax Fort Class Creation and Object Creation
'''
class Class_name:
    #attribute
    #methods

obj1 = Class_name(args)
obj2 = Class_name(args)
'''

class Car:
    def __init__(self,color,company,model,speed):
        self.color = color
        self.company = company
        self.model = model
        self.speed = speed
        self.new_launched()

    def new_launched(self):
        print("-------------------------------------")
        print("New Car Launched")
        print(self.__dict__)
        print("-------------------------------------")

    def Start(self):
        print(f"{self.model} Starting...")

    def Drive(self):
        self.Start()
        self.Accelerate()
        print(f"{self.model} Driving...")
        
        

    def Stop(self):
        print(f"{self.model}Stopping...")
        print("Speed : ",end=" ")
        for i in range(self.speed,-1,-1):
            print(i,"<-",end="")
        print()

    def Accelerate(self):
        print(f"{self.model} Accelerating...")
        print("Speed : ",end=" ")
        for i in range(0,self.speed+1):
            print("->",i,end="")
        print()

c1 = Car(color="Green",model="WAGON-R",company="TATA",speed=9)
c1.Drive()
c1.Stop()

c2 = Car(color="Red",model="Ferrari",company="Lamborgini",speed=20)
c2.Drive()
c2.Stop()

c1.speed = 12 # Modifying attribute
c1.Drive()
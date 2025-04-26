'''
__dict__   : Dictionary containing class's namespace
__doc__    : Class Documentation string
__class__   : Class Name
__module__ : Module namein which class is defined
__bases__  : List of base classes

'''


class Car:
    """
    A class to represent a Car.

    Attributes:
    -----------
    company : str
        The manufacturer of the car (e.g., Toyota, Ford).
    model : str
        The model name of the car (e.g., Corolla, Mustang).
    color : str
        The color of the car.
    speed : int
        The max speed of car

    Methods:
    --------
    new_launched():
        Prints the car's color, make, and model.
    
    Start():
        Simulates Starting the car by printing a message.

    Drive():
        Simulates driving the car by printing a message.

    Stop():
        Simulates Stopping the car by printing a message.

    Accelerate():
        Simulates Accelerating the car by printing a message.
    """

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

print(c1.__doc__)
print(c1.__dict__) #{'color': 'Green', 'company': 'TATA', 'model': 'WAGON-R', 'speed': 9}
print(c1.__module__) #__main__
print(c1.__class__) #<class '__main__.Car'>


# isinstance(object,class) : check that given objetc is object of the given class or not
class Demo:
    pass

print(isinstance(c1,Car)) #True
print(isinstance(c1,Demo)) #False




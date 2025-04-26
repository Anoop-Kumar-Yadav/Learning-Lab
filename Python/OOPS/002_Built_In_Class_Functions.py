'''
getattr(object_name,attribute_name)
setattr(object_name,attribute_name,new_value)
delattr(object_name,attricute_name)
hasattr(object_name,attrucute_name)

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

print(getattr(c1,"model")) #WAGON-R

print(getattr(c1,"speed")) #9
setattr(c1,"speed",15) 
print(getattr(c1,"speed")) #15

print(hasattr(c1,"wheel")) #False
print(hasattr(c1,"model"))  #True

print(hasattr(c1,"color")) #True
delattr(c1,"color")
print(hasattr(c1,"color")) #False



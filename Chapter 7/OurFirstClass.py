class Car: 
    #constructor 
    def __init__(self, color): 
        self.color = color 

    def motor(self, carType): 
        #1 = regular car 
        #2 = sports car 
        if carType == 1: 
            print("rev")
            
        elif carType == 2: 
            for i in range(2): 
                print("rev")
                
        else: 
            print("invalid") 

    def brakes(self): 
        print("stop") 

    def showColor(self): 
        print(f"Car color: {self.color}") 

#use car class 
normalCar = Car("green") 
normalCar.motor(1) 
normalCar.brakes() 
normalCar.showColor() 

print() 

#race car 
raceCar = Car("red") 
raceCar.motor(2) 
raceCar.brakes() 
raceCar.showColor() 
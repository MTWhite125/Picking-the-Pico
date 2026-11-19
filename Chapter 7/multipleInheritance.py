class Engine: 
    def rev(self): 
        print("rev") 

class Brakes: 
    def stop(self): 
    	print("stop") 

class Car: 
    def __init__(self): 
        self.engine = Engine() 
        self.brakes = Brakes() 

    def go(self): 
        self.engine.rev() 
        self.brakes.stop() 

car = Car() 
car.go()
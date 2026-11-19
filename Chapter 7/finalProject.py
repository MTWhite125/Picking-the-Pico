class Engine: 
    def rev(self): 
        print("rev") 

class Brakes: 
    def stop(self): 
        print("stop") 

class Car(Engine, Brakes): 

    def go(self): 
        self.rev() 
        self.stop() 

         

car = Car() 
car.go() 
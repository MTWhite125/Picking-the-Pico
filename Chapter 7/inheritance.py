class K9: 
    def poop(self): 
        print("poop") 

    def eat(self): 
        print("eat") 

    def sleep(self): 
        print("sleep") 

#Dog inherits from K9 
class Dog(K9): 
    def wagTail(self): 
        print("wag Tail") 

    def bark(self): 
        print("woof") 

foofy = Dog() 

foofy.eat() 
foofy.poop() 
foofy.bark() 
foofy.sleep() 
foofy.wagTail() 
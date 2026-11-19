class Dog: 
    def __init__(self, name): 
      # self links 'name' to this specific dog 
        self.name = name 

    def bark(self): 
        print(f"{self.name} says woof!") 

# 1. Create two distinct dog objects 
dog1 = Dog("Buddy") 
dog2 = Dog("Max") 
 
# 2. Call the method 
dog1.bark() 
dog2.bark() 
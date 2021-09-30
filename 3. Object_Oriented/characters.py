import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
#inherit character attributes
class Thief(Character):
    sneaky = "yes"
    
    def __init__(self, name, sneaky = True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    #methods are functions belong to a class -  always take at least one parameter
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0,1))
    
    def hide(self, light_level):
        return self.sneaky and light_level < 10
    

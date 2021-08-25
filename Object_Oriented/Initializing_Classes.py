import random

class Thief:
    sneaky = "yes"
    
    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    #methods are functions belong to a class -  always take at least one parameter
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0,1))
    
    def hide(self, light_level):
        return self.sneaky and light_level < 10

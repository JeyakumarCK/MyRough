import random

class Walker():
    
    def __init__(self, wdt, hgt):
        self.x = wdt/2
        self.y = hgt/2
        
    def step(self):
        choice = random.randint(0,4)
        if choice == 0 :
            x += 1
        elif choice == 1 :
            x -= 1
        elif choice == 2 :
            y += 1
        else:
            y -= 1
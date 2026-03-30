# I — Interface Segregation (ISP)
# 👉 Badi interface mat banao
class Worker:
    def work(self): pass
    def eat(self): pass
    
class Human(Worker):
    def work(self):
        print("Human Working...")
        
    def eat(self):
        print("Human Eating...")
        
class Robot(Worker):
    def work(self):
        print("Robot Working...")
        
    def eat(self):
        pass # Robot doesn't eat, but we are forced to implement this method

r = Robot()
r.work()
r.eat() # This is not ideal, as Robot doesn't eat

h = Human()
h.work()
h.eat()




# #############################################################################
# #############################################################################
class Workable:
    def work(self): pass

class Eatable:
    def eat(self): pass
    
class Human(Workable, Eatable):
    def work(self):
        print("Human Working...")
        
    def eat(self):
        print("Human Eating...")
        
class Robot(Worker):
    def work(self):
        print("Robot Working...")
        
    def eat(self):
        pass # Robot doesn't eat, but we are forced to implement this method

r = Robot()
r.work()
r.eat() # This is not ideal, as Robot doesn't eat

h = Human()
h.work()
h.eat()
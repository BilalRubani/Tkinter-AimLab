# An aim ball is a Simulton; it updates by shrinking over
#   a period of time, and when clicked, it will be removed
#   from the simulation; it will also be removed when its
#   dimensions reach a value of 0 as a result of shrinking.


from simulton import Simulton
from random import randint, choice

COLOR_LIST = ['red', 'blue', 'green', 'yellow', 'purple', 'black', 'brown', 'orange', 'pink'] 
class Aim(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        self.random_int = randint(3,6)
        self.color = choice(COLOR_LIST)
        Simulton.__init__(self, x, y, self.radius*self.random_int, self.radius*self.random_int)
        
    def update(self, model):
        self.change_dimension(-1, -1)
        if self.get_dimension() == (0,0):
            model.remove(self)

            
    def display(self,canvas):
        canvas.create_oval(self.get_location()[0] - self.get_dimension()[0]/2, self.get_location()[1] - self.get_dimension()[1]/2,
                                self.get_location()[0]+ self.get_dimension()[0]/2, self.get_location()[1] + self.get_dimension()[1]/2,
                                fill= self.color)     
            
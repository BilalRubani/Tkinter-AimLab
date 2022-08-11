# The reaction ball is derived from a Simulton base; it updates by resetting
#   its location periodically based on a period of time (7 ticks of the counter)
#   It's appearance is a black circle with a radius of 10 (e.g., a width/height 20).


from simulton import Simulton
from random   import randint


class Reaction(Simulton):  
    radius  = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, self.radius*2, self.radius*2)
        self._counter = 0
        
    def update(self, model):
        if self._counter == 7:
            self.set_location(randint(50, 900), randint(0, 450))
            self._counter = 0
        else:
            self._counter += 1
    
    def display(self,canvas):
        canvas.create_oval(self.get_location()[0] - self.get_dimension()[0]/2, self.get_location()[1] - self.get_dimension()[1]/2,
                                self.get_location()[0]+ self.get_dimension()[0]/2, self.get_location()[1] + self.get_dimension()[1]/2,
                                fill='black')
    

            

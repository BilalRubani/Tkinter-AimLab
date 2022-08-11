import controller
import model   # Calling update in update_all passes a reference to this model
from tkinter import messagebox

#Use the reference to this module to pass it to update methods

from reaction  import  Reaction
from aim   import  Aim
from random     import randint


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running      = False
total_clicks = 0
count        = 0
cycle_count  = 0
simultons    = set()
object_kind  = None
total_balls  = []


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons,count,total_clicks,total_balls
    running      = False
    cycle_count  = 0
    count        = 0
    total_clicks = 0
    simultons    = set()
    total_balls  = []


#start running the simulation
def start ():
    global running
    running = True
    if object_kind == None:
        messagebox.showinfo('Select a Mode','Please select a gamemode.')
    elif object_kind == 'Reaction':
        add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))
    else:
        add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))
        add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))
        add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global object_kind
    object_kind = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global total_clicks
    total_clicks += 1
    for s in set(simultons):
        if s.contains((x, y)):
            if object_kind == 'Aim': 
                remove(s)
                add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))
            global count
            count += 1 


#add simulton s to the simulation
def add(s):
    simultons.add(s)
    total_balls.append(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        if object_kind == 'Aim':
            if cycle_count % 12 == 0:
                add(eval(f"{object_kind}(randint(50, 900), randint(0, 450))"))
        if cycle_count == 500:
            if object_kind == 'Reaction':
                messagebox.showinfo('Game Over!', f'Your Score: {round(count/total_clicks, 2) * 100}% Accuracy')
                reset()
            else:
                messagebox.showinfo('Game Over!', f'Your Score: {round(count/len(total_balls), 2) * 100}% Accuracy')
                reset()
        for s in set(simultons):
            s.update(model)


#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    # Easier to delete all and display all; could use move with more thought
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(count)+" hit/"+str(total_clicks)+" clicks" if object_kind == 'Reaction' 
                                   else str(count)+" hit/"+str(len(total_balls))+" total_balls")
    
    


from tkinter import Tk,Frame,TOP,LEFT,BOTTOM,RAISED,BOTH

# import controller to call/create widgets and position them in the view
import controller


# Construct a simple root window
root = Tk()
root.title("Precision Testing")
root.protocol("WM_DELETE_WINDOW",quit)

frame = Frame(root)

# Place buttons simply at the top
frame.pack(side=TOP)
controller.reset_button (frame,text="Reset")     .pack(side=LEFT)
controller.start_button (frame,text="Start")     .pack(side=LEFT)
controller.object_button(frame,text="Reaction")  .pack(side=LEFT)
controller.object_button(frame,text="Aim")       .pack(side=LEFT)
controller.progress     (frame,text="0 updates/0 simultons",width=25,relief=RAISED).pack(side=LEFT)


 
# Place canvas in the space below
controller.simulation_canvas(root,width=900,height=500,bg="white").pack(side=BOTTOM,expand=True,fill=BOTH)

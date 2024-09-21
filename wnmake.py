import sys
from types import MethodType
# We won't hold anything tkinter related in this file. wnhandler will handle the tkinter part

print("wnmake")

#here the last 4 coordinates will be used when the object is sent forward to wnhandler
class window():
    def __init__(self, name, bgcolor, x1, y1, x2, y2):
        self.name = name
        self.bgcolor = bgcolor
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.shape = 0
        self.buttonlist = []

class button():
    def __init__(self, name, x1, y1, x2, y2, color, parent, parentcanvas):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.shapes = []
        self.parent = parent
        self.parentcanvas = parentcanvas
        self.function = 0
    def OnHover(self, event):                  
        self.parentcanvas.itemconfig(self.shapes[0], outline="red", width = 3)
    def UnHover(self, event):                  
        self.parentcanvas.itemconfig(self.shapes[0], outline="black", width = 1)
    def RunFunction(self, event):                  
        self.function()
        print("running function")

#Example of how this works
#testobj = createwindow("whatever", "green", height, width, "pausemenu", windowlist)
#second last arg is "regular" or "pausemenu"     
#last arg is a list to hold the windows 
def createwindow(name, bgcolor, height, width, ttype, windowlist):
    if ttype == "base":
        x1, y1 = 0, 0
        x2, y2 = width, height
        y2 = height
    if ttype == "overlap":
        x1, y1 = 50, 50
        width = width - 50
        height = height - 50
        x2, y2 = width, height
    new_window = window(name, bgcolor, x1, y1, x2, y2)
    windowlist.append(new_window)
    return new_window
    
def createbutton(name, width, height, dx, dy, ttype, parent, parentcanvas, function):
    x1 = 0 + dx
    x2 = width + dx
    y1 = 0 + dy
    y2 = height + dy
    color = "grey"
    newbutton = button(name, x1, y1, x2, y2, ttype, parent, parentcanvas)
    for i in functionlist:
        if function == i.__name__:
            print("MATCH")
            newbutton.function = MethodType(i, newbutton)
    parent.buttonlist.append(newbutton)
    return newbutton
    
def exit(event):
    print("whatever")
    sys.exit()

functionlist = [exit]
print("functionlist", functionlist)
print("functionlist0", functionlist[0])
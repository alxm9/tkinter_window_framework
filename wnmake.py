import sys
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
        self.buttonlist = []

class button():
    def __init__(self, name, x1, y1, x2, y2, color, parent, function):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.parent = parent
        self.function = function

#Example of how this works
#testobj = createwindow("whatever", "green", height, width, "pausemenu")
#last arg is "regular" or "pausemenu"        
def createwindow(name, bgcolor, height, width, ttype):
    if ttype == "regular":
        x1, y1 = 0, 0
        x2, y2 = width, height
        y2 = height
    if ttype == "pausemenu":
        x1, y1 = 50, 50
        width = width - 50
        height = height - 50
        x2, y2 = width, height
    new_window = window(name, bgcolor, x1, y1, x2, y2)
    return new_window
    
def createbutton(name, width, height, dx, dy, color, parent, function):
    x1 = 0 + dx
    x2 = width + dx
    y1 = 0 + dy
    y2 = height + dy
    newbutton = button(name, x1, y1, x2, y2, color, parent, function)
    return newbutton
    
def exit():
    pass
   # sys.exit()
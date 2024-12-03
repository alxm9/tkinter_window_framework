import sys
### to del
from tkinter import *
width = 500 
height = 500 
interface = Tk()
interface.geometry(f"{height}x{width}")
canvas = Canvas(width=width, height=height)
canvas.pack()
###

class Window():
    def __init__(self, name, wintype):
        self.name = name
        self.wintype = wintype
        self.graphics = [] #canvas objects
        self.objects = [] #buttons, other

        if wintype == "fullscreen":
            x0, y0 = 0, 0
            x1, y1 = width, height
        if wintype == "overlay":
            x0, y0 = width/4, height/4
            x1, y1 = (width/4)*3, (height/4)*3

        bg = canvas.create_rectangle(x0,y0,x1,y1, fill="orange")
        self.graphics.append(bg)


    def create_button(self, name, xcord = 0, ycord = 0, method = False, width = 100, height = 50):
        self.objects.append(Button(name, xcord, ycord, method, width, height, self))

    def destroy(self):
        for graphic in self.graphics:
            canvas.delete(graphic)
        # canvas.delete(graphic for graphic in self.graphics) # can't take generator items as an arg
        for object in self.objects:
            for graphic in object.graphics:
                canvas.delete(graphic)
        del self

class Button():
    def __init__(self, name, xcord, ycord, method, width, height, parent):
        self.name = name
        self.parent = parent
        self.xcord, self.ycord = xcord, ycord
        self.graphics = [] #canvas objects
        self.method = self.assign_method(method) if method != False else False

        x0, y0 = 0+xcord, 0+ycord
        x1, y1 = width+xcord, height+ycord

        button_shape = canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline = "black")
        self.graphics.append(button_shape)
        self.hover_behaviour()
        button_text = canvas.create_text(x0+(width/2),y0+(height/2), text=name, font=("sans-serif",15), state='disabled')
        self.graphics.append(button_text)
    
    def hover_behaviour(self):
        for graphic in self.graphics:
            canvas.tag_bind(graphic, '<Enter>', self.OnHover)
            canvas.tag_bind(graphic, '<Leave>', self.UnHover)
            canvas.tag_bind(graphic, '<ButtonRelease>', self.method)

    def assign_method(self,method):
        if method[:6] == 'target':
            arg = method.split('_',1)[1]
            method = 'target'
        return {
            'exit': lambda _: sys.exit(),
            'target': lambda _: create_menu(arg),
            'destroy': lambda _: self.parent.destroy()
        }[method]
    
    def OnHover(self, event):
        print("hello")
    
    def UnHover(self, event):
        print("goodbye")



def bring_to_front(): # draws window and its objects
    pass

def create_menu(menu):
    match menu:
        case "mainmenu":
            mainmenu = Window("mainmenu","fullscreen")
            mainmenu.create_button("Exit",xcord = 100,ycord = 200, method='exit')
            mainmenu.create_button("pausemenu",xcord = 100,ycord = 350, method='target_pausemenu')
        case "pausemenu":
            pausemenu = Window("pausemenu","overlay")
            pausemenu.create_button("Exit",xcord = 200,ycord = 150, method='exit')
            pausemenu.create_button("Return",xcord = 200,ycord = 300, method='destroy')


create_menu('mainmenu')

interface.mainloop()
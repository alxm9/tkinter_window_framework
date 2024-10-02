print("wnhandler - brother of wnmake \nnada \n")

    
def drawwindow(window, canvas, current_window, previous_window):
    print("CURRENT_WINDOW", current_window)
    print("previous_window", previous_window)
    for i in current_window.buttonlist:
        for d in i.shapes:
            canvas.delete(d)
    previous_window = current_window
    current_window = window
    window.shape = canvas.create_rectangle((window.x1,window.y1,window.x2,window.y2), fill=window.bgcolor, width = 0)
    for i in window.buttonlist:
        i.shapes.append(canvas.create_rectangle((i.x1, i.y1, i.x2, i.y2), fill=i.color, width = 1))
        i.shapes.append(canvas.create_text(i.x1+50,i.y1+25,text=i.name, font=("Arial", 12),  fill = "black"))
        for d in i.shapes:
            canvas.tag_bind(d, '<Enter>', i.OnHover)
            canvas.tag_bind(d, '<Leave>', i.UnHover)
            canvas.tag_bind(d, '<ButtonRelease>', i.RunFunction)
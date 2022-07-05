import tkinter as tk
def draw(canvas):
    pass

def makeCanvas(w,h):
    root = tk.Tk()
    
    
    canvas =tk.Canvas(root,width = w, height = h, background = 'gray')
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas)
    
    root.mainloop()
    
#makeCanvas(400,500)
makeCanvas(1000,5000)
    


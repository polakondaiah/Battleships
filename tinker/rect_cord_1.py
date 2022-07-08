import tkinter as tk


def makeCanvas(w,h):
    root = tk.Tk()
    
    
    canvas =tk.Canvas(root,width = w, height = h, background = 'gray')
    canvas.configure(bd=0, highlightthickness=0)
  #  canvas.create_rectangle(0,0,10,10, fill="blue")
   # canvas.create_rectangle(0,1,20,20, fill="blue")
   # canvas.create_rectangle(0,2,50,50, fill="blue")
    canvas.create_rectangle(0,50,50,150, fill="blue")
    canvas.pack()
    
    
    root.mainloop()
    
#makeCanvas(400,500)
makeCanvas(1000,5000)
    
import tkinter as tk
from tkinter import ttk
win=tk.Tk()

win.title('Events')
menu=tk.Menu(win,tearoff=False)
menu.add_command(label="Nothing...")
def popup(event):
     menu.tk_popup(event.x,event.y)
win.bind("<Button-3>",popup)
win.mainloop()
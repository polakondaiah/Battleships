import tkinter as tk
from tkinter import ttk
win=tk.Tk()
def get_event(event):
     print(f"{event.x} {event.y}")
win.bind("<Button-3>",get_event)
win.mainloop()
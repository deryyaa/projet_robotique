import tkinter as tk
from Robot import Robot
window = tk.Tk()
#window.geometry("500x500")
cnv = tk.Canvas(window, width=600, height=400,
bg='ivory')
cnv.pack(padx=50, pady=50) #marge en y et x
window.mainloop()

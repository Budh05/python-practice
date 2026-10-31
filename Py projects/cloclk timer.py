import tkinter as tk
import time
def update():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000, update)
root=tk.Tk()
root.title("Clock Timer")
label=tk.Label(root, font=("Arial", 80), bg="orange", fg="white")
label.pack(padx=40, pady=40)
update()
root.mainloop()
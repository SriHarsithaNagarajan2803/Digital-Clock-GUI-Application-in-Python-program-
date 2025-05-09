from tkinter import *
from time import strftime

root = Tk()
root.title('Digital Clock')

def time_display():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time_display)

label = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time_display()
root.mainloop()

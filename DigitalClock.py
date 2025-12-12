import tkinter as t
from time import strftime

root = t.Tk()
root.title("Clock by Taibullah Shikdar")
root.geometry("400x200")
root.resizable(False, False)


def time():
    string = strftime("%H:%M:%S \n%D")
    label.config(text=string)
    label.after(1000, time)


label = t.Label(root, font=("Helvetica", 48), fg="white", bg="black")
label.pack(anchor='center')
root.configure(bg="black")
time()
root.mainloop()

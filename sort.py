import time
import tkinter.messagebox
from tkinter import *
import pyshorteners

short = pyshorteners.Shortener()
window = Tk()


def click():
    url = str(inputField.get())
    result = short.tinyurl.short(url)
    window.clipboard_append(result)
    tkinter.messagebox.showinfo(title="Shorted Url is Copied !", message=result)


window.config(bg="black")
window.title("Link Short")
title = Label(text="Link sort-ner", font=("ariel", 15, "italic"), bg="#393939", fg="blue")
title.grid(column=1, row=0, columnspan=3)
link = Label(text="Enter Your URL", font=("ariel", 12, "bold"), bg="#393939", fg="white")
link.grid(column=1, row=1)
inputField = Entry(width=50)
inputField.grid(column=2, row=1, columnspan=2)
button = Button(text="Click Me", fg="white", bg="green")
button.grid(column=2, row=2)
button.config(pady=10, padx=10, command=click)

window.mainloop()

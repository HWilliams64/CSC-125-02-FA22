from tkinter import *

total = 0

def click():
    global total
    total += 1
    print(f"The button is clicked {total} times")

window = Tk()

window.title("Python Example GUI")

window.geometry('500x300')

label = Label(window, text="Hello my pythoners", font=('Arial Bold', 15))

label.grid(column=1, row=0)

button = Button(window, text="Click me", command=click)

button.grid(column=0, row=0)

window.mainloop()
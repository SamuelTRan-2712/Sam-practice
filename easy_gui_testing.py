from tkinter import *
import tkinter
from tkinter import messagebox


def sams_calculator():
    try:
        number1 = Entry.get(E1)
        number2 = Entry.get(E2)
        operator = Entry.get(E3)
        number1 = int(number1)
        number2 = int(number2)

        if operator == "+":
            result = number1 + number2
        if operator == "-":
            result = number1 - number2
        if operator == "/":
            result = number1 / number2
        if operator == "*":
            result = number1 * number2
        Entry.insert(E4, 0, result)
        print(result)
    except ValueError:
        messagebox.showinfo("Error warning", "please enter integers only")


top = tkinter.Tk()


L1 = Label(top, text="Sam's small calculator", foreground="red").grid(row=0, column=1)
L2 = Label(top, text="number 1", background="yellow", foreground="blue").grid(row=1, column=0)
L3 = Label(top, text="number 2", background="yellow", foreground="blue").grid(row=2, column=0)
L4 = Label(top, text="operator", background="green", foreground="white").grid(row=3, column=0)
L5 = Label(top, text="result").grid(row=4, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)

B = Button(top, text="get result", command=sams_calculator).grid(rows=5, column=1)

top.mainloop()

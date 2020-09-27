import math as m
from tkinter import *

window = Tk()
window.title("SCIENTIFIC CALCULATOR")  # This is the heading for the calculator
# e is the input window
e = Entry(window, width=75, borderwidth=5, relief=RIDGE, fg="white", bg="Black")
e.grid(row=0, columnspan=5, padx=10, pady=25)


# this is function to print in the screen
def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)
    return


# this function for importing  scientific functions for buttons
def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    if text == 'deg':
        result = str(m.degrees(float(no)))
    if text == 'sin':
        result = str(m.sin(float(no)))
    if text == 'cos':
        result = str(m.cos(float(no)))
    if text == 'tan':
        result = str(m.tan(float(no)))
    if text == 'log':
        result = str(m.log10(float(no)))
    if text == 'ln':
        result = str(m.log(float(no)))
    if text == 'sqrt':
        result = str(m.sqrt(float(no)))
    if text == 'x!':
        result = str(m.factorial(float(no)))
    if text == '1/x':
        result = str(1 / (float(no)))
    if text == '%':
        result = str(m.modf(float(no)))

    if text == 'pi':
        if no == "":
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    if text == 'e':
        if no == "":
            result = str(m.e)
        else:
            result = str(m.e ** float(no))

    e.delete(0, END)
    e.insert(0, result)


def clear():  # This function for clearing the screen
    e.delete(0, END)
    return


def bksps():
    current = e.get()
    length = len(current) - 1  # this is for deleting one digit from screen
    e.delete(length, END)


def evaluate():  # This function store the answer and delete the input and show the answer
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


# keys  in first row
back = Button(text='DEL', relief=RAISED, bg='Red', fg='white', command=lambda: bksps(), padx=20, pady=5)
AC = Button(text='AC', relief=RAISED, bg='Red', fg="White", command=lambda: clear(), padx=29, pady=5)

# keys  in second row
sqrt = Button(text='sqrt', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
sqrt.bind("<Button-1>", sc)
sqr = Button(text='sqr', relief=RAISED, bg='black', fg='white', padx=29, pady=10, command=lambda: click("^"))
log = Button(text='log', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
log.bind("<Button-1>", sc)
ln = Button(text='ln', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
ln.bind("<Button-1>", sc)
deg = Button(text='deg', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
deg.bind("<Button-1>", sc)

# keys  in third row
sin = Button(text='sin', relief=RAISED, bg='black', fg='white', padx=32, pady=10)
sin.bind("<Button-1>", sc)
cos = Button(text='cos', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
cos.bind("<Button-1>", sc)
tan = Button(text='tan', relief=RAISED, bg='black', fg='white', padx=29, pady=10)
tan.bind("<Button-1>", sc)
fac = Button(text='x!', relief=RAISED, bg='black', fg='white', padx=30, pady=10)
fac.bind("<Button-1>", sc)
inv = Button(text='1/x', relief=RAISED, bg='black', fg='white', padx=31, pady=10)
inv.bind("<Button-1>", sc)

# keys  in 4th row
seven = Button(text='7', relief=RAISED, bg='gray', fg='white', padx=32, pady=10, command=lambda: click("7"))
eight = Button(text='8', relief=RAISED, bg='gray', fg='white', padx=29, pady=10, command=lambda: click("8"))
nine = Button(text='9', relief=RAISED, bg='gray', fg='white', padx=29, pady=10, command=lambda: click("9"))
plus = Button(text='+', relief=RAISED, bg='black', fg='white', padx=30, pady=10, command=lambda: click("+"))
div = Button(text='/', relief=RAISED, bg='black', fg='white', padx=31, pady=10, command=lambda: click("/"))

# keys  in 5th row
four = Button(text='4', relief=RAISED, bg='gray', fg='white', padx=32, pady=10, command=lambda: click("4"))
five = Button(text='5', relief=RAISED, bg='gray', fg='white', padx=29, pady=10, command=lambda: click("5"))
six = Button(text='6', relief=RAISED, bg='gray', fg='white', padx=29, pady=10, command=lambda: click("6"))
subs = Button(text='-', relief=RAISED, bg='black', fg='white', padx=30, pady=10, command=lambda: click("-"))
mult = Button(text='*', relief=RAISED, bg='black', fg='white', padx=31, pady=10, command=lambda: click("*"))


# keys gride in first row
back.grid(row=1, column=0)
AC.grid(row=1, column=4)

# keys gride in second row
sqrt.grid(row=2, column=0)
sqr.grid(row=2, column=1)
log.grid(row=2, column=2)
ln.grid(row=2, column=3)
deg.grid(row=2, column=4)

# keys gride in third row
sin.grid(row=3, column=0)
cos.grid(row=3, column=1)
tan.grid(row=3, column=2)
fac.grid(row=3, column=3)
inv.grid(row=3, column=4)

# keys gride in 4th row
seven.grid(row=4, column=0)
eight.grid(row=4, column=1)
nine.grid(row=4, column=2)
plus.grid(row=4, column=3)
div.grid(row=4, column=4)

# keys gride in 5th row
four.grid(row=5, column=0)
five.grid(row=5, column=1)
six.grid(row=5, column=2)
subs.grid(row=5, column=3)
mult.grid(row=5, column=4)

window.mainloop()

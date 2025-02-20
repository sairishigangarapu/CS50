"""u are the python file or code"""
from tkinter import *
import tkinter as tk


res = op1 = op2 = operation = ''

# code for input
def input_num(digit):
    global op1, op2
    tb1.insert(len(tb1.get()) + 1, digit)
    if op1 == '':
        op1 = tb1.get()

    else:
        op2 = tb1.get()


def input_decimal(decimal):
    tb1.insert(len(tb1.get())+1, decimal)


def input_pie(pie):
    tb1.insert(len(tb1.get())+1, pie)


def square():
    x = float(tb1.get())
    res = x*x
    tb1.delete(0, END)
    tb1.insert(0, 'Ans = ' + str(res))


def cal(choice):
    global operation, op1, op2
    if op2 == '':
        operation = choice
        tb1.delete(0, END)
        tb1.insert(0, "")
    else:
        tb1.delete(0, END)
        tb1.insert(0, "")
        if operation == '+':
            op1 = float(op1) + float(op2)
        elif operation == '-':
            op1 = float(op1) - float(op2)
        elif operation == '*':
            op1 = float(op1) * float(op2)
        elif operation == '/':
            op1 = float(op1) / float(op2)
        op2 = ''
        operation = choice


def reset():
    global operation, op1, op2
    operation = op1 = op2 = ""
    tb1.delete(0, END)
    tb1.insert(0, "")


def result():
    global op2, res, op1
    op2 = tb1.get()
    if operation == '+':
        res = float(op1) + float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '-':
        res = float(op1) - float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '*':
        res = float(op1) * float(op2)
        op1 = res
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == '/':
        if float(op2) == 0:
            res = 'Division by Zero Error!'
            tb1.delete(0, END)
            tb1.insert(0, 'Ans = ' + str(res))
        else:
            res = float(op1) / int(op2)
            tb1.delete(0, END)
            tb1.insert(0, 'Ans = ' + str(float(res)))
    elif operation == 'x*x':
        res = int(op1) / int(op2)
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(float(res)))
    else:
        res = 'Error!'
        tb1.delete(0, END)
        tb1.insert(0, 'Ans = ' + str(res))


root = tk.Tk()
root.geometry("500x700")  # More compact size
root.title("Calculator")
root.configure(bg='#E8E8E8')  # Light gray background
root.resizable(False, False)

# Style constants
BUTTON_FONT = ("Arial", 20, "bold")
DISPLAY_FONT = ("Arial", 30)
BUTTON_COLOR = "#FFFFFF"  # White
OPERATOR_COLOR = "#FFB74D"  # Orange
SPECIAL_COLOR = "#9575CD"  # Purple
EQUAL_COLOR = "#4CAF50"  # Green

# Calculator display
tb1 = tk.Entry(root,
    width=20,
    font=DISPLAY_FONT,
    justify='right',
    bd=10,
    relief='sunken'
)
tb1.pack(padx=20, pady=20, fill='x')

# Button frame
button_frame = Frame(root, bg='#E8E8E8')
button_frame.pack(padx=20, pady=10, expand=True)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'π', '+'],
    ['x²', 'C', '=']
]

# Create and place buttons
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text in ['+', '-', '*', '/']:
            bg_color = OPERATOR_COLOR
        elif btn_text in ['x²', 'π']:
            bg_color = SPECIAL_COLOR
        elif btn_text == '=':
            bg_color = EQUAL_COLOR
        else:
            bg_color = BUTTON_COLOR

        btn = Button(
            button_frame,
            text=btn_text,
            width=4,
            height=1,
            font=BUTTON_FONT,
            bd=5,
            relief='raised',
            bg=bg_color
        )

        # Command binding
        if btn_text.isdigit():
            btn.configure(command=lambda x=btn_text: input_num(x))
        elif btn_text == '.':
            btn.configure(command=lambda: input_decimal('.'))
        elif btn_text == 'π':
            btn.configure(command=lambda: input_pie(3.14))
        elif btn_text == 'x²':
            btn.configure(command=square)
        elif btn_text == 'C':
            btn.configure(command=reset)
        elif btn_text == '=':
            btn.configure(command=result)
        else:
            btn.configure(command=lambda x=btn_text: cal(x))

        # Grid layout
        btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')

# Configure grid weights
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()

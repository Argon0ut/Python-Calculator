import tkinter as tk
from tkinter import messagebox

#MAINLOOP SETTINGS
window = tk.Tk()
window.title("First Calculator Project")
photo = tk.PhotoImage(file='icon.png')
window.iconphoto(False, photo)
window.config(bg='purple')
window.geometry(f"240x270+100+200")

def add_digit(digit):
    enteredValue = calc.get()
    if enteredValue == '0' and len(enteredValue)==1:
        enteredValue = enteredValue[1:]
    calc.delete(0, tk.END)
    calc.insert(0, enteredValue+digit)

def add_operation(operation):
    enteredValue = calc.get()
    if enteredValue[-1] in '+-*/':
        enteredValue = enteredValue[:-1]
    elif '+' in enteredValue or '-' in enteredValue or '/' in enteredValue or '*' in enteredValue:
        calculate()
        enteredValue=calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, enteredValue+operation)

def calculate():
    enteredValue = calc.get()
    if enteredValue[-1] in '+-/*':
        enteredValue = enteredValue+enteredValue[:-1]
    calc.delete(0,tk.END)
    try:
        calc.insert(0, eval(enteredValue))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Вводите только цифры')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя, попробуйте еще раз.')
def clear():
    calc.delete(0, tk.END)
    calc.insert(0,'0')
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda : add_digit(digit))
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
window.bind('<Key>', press_key)

calc = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick='we')
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=1 , stick='wens', padx=5, pady=5)
make_calc_button('=').grid(row=4, column=3 , stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=2 , stick='wens', padx=5, pady=5)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)

window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)
window.mainloop()
from tkinter import *

root = Tk()
root.title('- Calculator-DESPA1-')
entry_field = Entry(root, width=40)
entry_field.grid(row=0, column=1, columnspan=3)


def buton(number):
    """
    this function writes a number in the calculator entry field
    :param number:
    :return: none
    """
    curent = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(curent) + str(number))

def buton_clear():
    """
    this function deletes the value from the entry field
    :return: none
    """
    entry_field.delete(0, END)


def buton_egal():
    """
    this function is used to perform mathematical operations

    :return: none
    """
    second_number = entry_field.get()
    entry_field.delete(0, END)
    if math == 'addition':
        entry_field.insert(0, f_num + int(second_number))
    elif math == 'minus':
        entry_field.insert(0, f_num - int(second_number))
    elif math == 'multiplycation':
        entry_field.insert(0, f_num * int(second_number))
    elif math == 'division':
        entry_field.insert(0, f_num / int(second_number))

def buton_plus():
    """
    this function is used to set the addition operation
    :return: none
    """
    first_number = entry_field.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry_field.delete(0, END)

def buton_minus():
    """
    this function is used to set the subtraction operation

    :return: none
    """
    first_number = entry_field.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(first_number)
    entry_field.delete(0, END)


def buton_multiply():
    """
    this function is used to set the multiplication operation
    :return: none
    """

    first_number = entry_field.get()
    global f_num
    global math
    math = 'multiplycation'
    f_num = int(first_number)
    entry_field.delete(0, END)

def buton_divide():
    """
    this function is used to set the division operation
    :return: none
    """
    first_number = entry_field.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry_field.delete(0, END)


buton_1 = Button(root, padx=40, pady=30, text="1", font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(1))
buton_2 = Button(root, padx=40, pady=30, text='2', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(2))
buton_3 = Button(root, padx=40, pady=30, text='3', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(3))
buton_4 = Button(root, padx=40, pady=30, text='4', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(4))
buton_5 = Button(root, padx=40, pady=30, text='5', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(5))
buton_6 = Button(root, padx=40, pady=30, text='6', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(6))
buton_7 = Button(root, padx=40, pady=30, text='7', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(7))
buton_8 = Button(root, padx=40, pady=30, text='8', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(8))
buton_9 = Button(root, padx=40, pady=30, text='9', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(9))
buton_0 = Button(root, padx=40, pady=30, text='0', font=30, bg='white', fg='black', borderwidth=15, command=lambda: buton(0))
buton_clear = Button(root, padx=40, pady=20, text='clear', font=30, bg='white', fg='blue', borderwidth=15, command=buton_clear)
buton_plus = Button(root, padx=40, pady=20, text='+', font=30, bg='white', fg='black', borderwidth=15, command=buton_plus)
buton_egal = Button(root, padx=40, pady=20,  text='=', font=30, bg='green', fg='black', borderwidth=15, command=buton_egal)
buton_minus = Button(root, padx=40, pady=20, text='-', font=30, bg='white', fg='black', borderwidth=15,  command=buton_minus)
buton_multiply = Button(root, padx=40, pady=20, text='*', font=30, bg='white', fg='black', borderwidth=15, command=buton_multiply)
buton_divide = Button(root, padx=40, pady=20, text='/', font=30, bg='white', fg='black', borderwidth=15, command=buton_divide)

buton_1.grid(row=4, column=1)
buton_2.grid(row=4, column=2)
buton_3.grid(row=4, column=3)
buton_4.grid(row=3, column=1)
buton_5.grid(row=3, column=2)
buton_6.grid(row=3, column=3)
buton_7.grid(row=2, column=1)
buton_8.grid(row=2, column=2)
buton_9.grid(row=2, column=3)
buton_0.grid(row=5, column=1)
buton_clear.grid(row=5, column=2)
buton_plus.grid(row=5, column=3)
buton_egal.grid(row=8, column=1)
buton_minus.grid(row=7, column=1)
buton_multiply.grid(row=7, column=2)
buton_divide.grid(row=7, column=3)

root.mainloop()

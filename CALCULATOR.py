from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("ERROR")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("∞")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""   

window = Tk()
window.title("KARTIK'S CALCULATOR")
window.geometry("450x510")
window.configure(bg="black")

equation_text = ""
equation_label = StringVar()

label_1 = Label(window, text="AIRTHEMATIC CALCULATOR", font="consolas 25 bold italic underline", fg="red", bg="light green", anchor="center", borderwidth=4, relief="ridge")
label_1.pack(fill="x")

label = Label(window, textvariable=equation_label, font="consolas 20 bold", fg="black", bg="white", anchor="w", height=2, borderwidth=5, relief="ridge")
label.pack(fill="x")

frame = Frame(window, bg="black")
frame.pack()

button1 = Button(frame, text=1, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(1))
button1.grid(row=0, column=0, padx=5,pady=5)

button2 = Button(frame, text=2, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(2))
button2.grid(row=0, column=1, padx=5,pady=5)

button3 = Button(frame, text=3, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(3))
button3.grid(row=0, column=2, padx=5,pady=5)

button4 = Button(frame, text=4, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(4))
button4.grid(row=1, column=0, padx=5,pady=5)

button5 = Button(frame, text=5, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(5))
button5.grid(row=1, column=1, padx=5,pady=5)

button6 = Button(frame, text=6, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(6))
button6.grid(row=1, column=2, padx=5,pady=5)

button7 = Button(frame, text=7, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(7))
button7.grid(row=2, column=0, padx=5,pady=5)

button8 = Button(frame, text=8, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(8))
button8.grid(row=2, column=1, padx=5,pady=5)

button9 = Button(frame, text=9, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(9))
button9.grid(row=2, column=2, padx=5,pady=5)

button0 = Button(frame, text=0, height=3, width=8, font="consolas 15 bold", bg="orange", command=lambda: button_press(0))
button0.grid(row=3, column=1, padx=5,pady=5)

plus = Button(frame, text='+', height=3, width=8, font="consolas 15 bold", bg="lightblue", command=lambda: button_press('+'))
plus.grid(row=0, column=3, padx=5,pady=5)

minus = Button(frame, text='-', height=3, width=8, font="consolas 15 bold", bg="lightblue", command=lambda: button_press('-'))
minus.grid(row=1, column=3, padx=5,pady=5)

multiply = Button(frame, text='*', height=3, width=8, font="consolas 15 bold", bg="lightblue", command=lambda: button_press('*'))
multiply.grid(row=2, column=3, padx=5,pady=5)

divide = Button(frame, text='/', height=3, width=8, font="consolas 15 bold", bg="lightblue", command=lambda: button_press('/'))
divide.grid(row=3, column=3, padx=5,pady=5)

equal = Button(frame, text='=', height=3, width=8, font="consolas 15 bold", bg="lightblue", command=equals)
equal.grid(row=3, column=2, padx=5,pady=5)

clear = Button(frame, text='C', height=3, width=8, font="consolas 15 bold", bg="black",fg="red", command=clear)
clear.grid(row=3, column=0, padx=5,pady=5)

window.mainloop()

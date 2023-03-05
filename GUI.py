from tkinter import *
import tokenizer as token
import solver as solve
import Quantizer as Quanta
import pygame

# import BODMAS as Bd

root = Tk()
root.title("calculator program")
root.config(bg="orange")
root.geometry("500x500")

equation_text = ""

equation_label = StringVar()
label = Label(root, textvariable=equation_label, font=('consolas', 20), bg="#ffddff", width=24, height=2)
label.pack()

frame = Frame(root)
frame.pack()

pygame.mixer.init()


def play_sound():
   pygame.mixer.music.load("C:/Users/1008tu/OneDrive/Documents/Full-stack_web-dev/Drum-kit/sounds/mixkit-retro-game-notification-212.mp3")
   pygame.mixer.music.play()


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
    except ZeroDivisionError:
        total = "Undefined"
    except SyntaxError:
        total = "Invalid Syntax"
    equation_label.set(total)
    equation_text = total


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


button1 = Button(frame, text=1, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(1), play_sound()])
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(2), play_sound()])
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(3), play_sound()])
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(4), play_sound()])
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(5), play_sound()])
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(6), play_sound()])
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(7), play_sound()])
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(8), play_sound()])
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(9), play_sound()])
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press(0), play_sound()])
button0.grid(row=3, column=0)

plus = Button(frame, text='+', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press('+'), play_sound()])
plus.grid(row=0, column=3)
minus = Button(frame, text='-', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press('-'), play_sound()])
minus.grid(row=1, column=3)
multiply = Button(frame, text='*', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press('*'), play_sound()])
multiply.grid(row=2, column=3)
divide = Button(frame, text='/', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press('/'), play_sound()])
divide.grid(row=3, column=3)
equal = Button(frame, text='=', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [equals(), play_sound()])
equal.grid(row=3, column=2)
decimal = Button(frame, text='.', fg="orange", bg="black", height=4, width=9, font=35, command=lambda: [button_press('.'), play_sound()])
decimal.grid(row=3, column=1)  # change integer to float in solver
clears = Button(root, text='clear', fg="orange", bg="black", height=4, width=15, font=35, command=lambda: [clear(), play_sound()])
clears.pack()

root.mainloop()

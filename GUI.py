from tkinter import *
import tokenizer as token
import solver as solve
import Quantizer as Quanta
import BODMAS as Bd

root = Tk()
e = Entry(root)
e.pack()

def myClick():
    Input = e.get()
    lis = token.Tokenizer.tokens(Input)
    lis = Quanta.Quantizer.Quartz(lis)
    #lis = Bd.BODMAS.bodmas(e.get())
    #print('+' in lis)
    var1, var2, var3 = lis[0][0], lis[0][1], lis[0][2]
    ans = solve.Solver.calculator(var1, var2, var3)
    myLabel = Label(root, text = Input + ' = '  +str(ans))
    myLabel.pack()

myButton = Button(root, text="=", command=myClick)
myButton.pack()

root.mainloop()

from tkinter import *
import tkinter
import math
import tkinter.messagebox
import random

window = tkinter.Tk()
window.geometry("550x350")

number1 = random.randint(1,20)
number2 = random.randint(1,10)

def numberguess():
    value = int(takeguess.get())
    productguess = number1 * number2
    if value > productguess:
        tkinter.messagebox.showinfo("Guessing Box","Your guess is too high")
    if value < productguess:
        tkinter.messagebox.showinfo("Guessing Box","Your guess is too low")
    elif value == productguess:
        tkinter.messagebox.showinfo("Good Guessing Box","You guess the number correctly!")
        window.quit()



tkinter.messagebox.showinfo("message","Guess the product of the two \n random numbers one of the random numbers is shown \n \
you have to guess the second number and \n enter the final product of the two numbers")

guessingame = Label(window,text = "Guessing Game!")

takeguess = Entry(window,width = 7)
num1 = Label(window,text = str(number1) + " x _ ?")
info = Label(window,text = "The random number which you have to multiply the shown number by \n \
is in the 1-10 range")

takebtn = Button(window,text = "Guess",command = numberguess)




takeguess.place(x = 185, y = 250)

takebtn.place(x = 265, y = 250)
num1.place(x = 250, y = 220)
info.place(x = 60, y = 180 )

guessingame.place(x = 220, y = 25)

    
window.mainloop()

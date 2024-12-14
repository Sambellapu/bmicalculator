from tkinter import *

win = Tk()
win.geometry("400x400")


def bmi():
    h = s1.get()
    w = s2.get()
    b = w / (h ** 2)
    bmi2.set(b)

    if b < 18.5:
        l4.config(text="You are underweight", bg="red")
    elif b < 25:
        l4.config(text="You are heathy", bg="green")
    else:
        l4.config(text="You are overweight", bg="red")


l1 = Label(text="BMI Calculator")

l2 = Label(text="Select hight in meters")

s1 = Scale(from_=0, to=3, orient=HORIZONTAL, resolution=0.01)

l3 = Label(text="Select weight in kgs")

s2 = Scale(from_=0, to=250, orient=HORIZONTAL, resolution=0.01)

b1 = Button(text="Get BMI", command=bmi)

bmi2 = DoubleVar()

s3 = Scale(from_=0, to=50, variable=bmi2, orient=HORIZONTAL, resolution=0.01)

l4 = Label()

l1.pack()
l2.pack()
s1.pack()
l3.pack()
s2.pack()
b1.pack()
s3.pack()
l4.pack()
win.mainloop()
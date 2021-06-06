from tkinter import*
top= Tk()
top.title("simple calculator")
top.resizable(0,0)
#_____window lable_____
cal= Label(top,text="simple calculator")
cal.grid(row=0,columnspan=8)
#_____variables____
var=""
output_var=StringVar()

#_____to show output feild_____
result= Entry(top, textvariable=output_var)
result.grid(row=2,columnspan=10)
result.focus()

#_____calculations input______
def calcu(input):
    try:
        global var
        var=var+str(input)
        output_var.set(var)
    except:
        output_var.set("error")

#_____calculations output_____
def answer():
    try:
        global var 
        output=str(eval(var))
        output_var.set(output)
        var=""
    except:
        output_var.set("error")

#____clear____
def clear():
    try:
        global var
        output_var.set("")
    except:
        output_var.set("error")

# ______buttons_______

button1 = Button(top,text="1",  command =lambda: calcu(1),height=1, width=4, )
button1.grid(row=6, column=1,padx=5,pady=5)

button2 = Button(top, text="2",  command=lambda:calcu(2),height=1, width=4)
button2.grid(row=6, column=2,padx=5,pady=5 )

button3 = Button(top, text="3", command=lambda:calcu(3),height=1, width=4)
button3.grid(row=6, column=3,padx=5,pady=5)

button4 = Button(top, text="4",  command=lambda:calcu(4),height=1, width=4)
button4.grid(row=5, column=1,padx=5,pady=5)

button5 = Button(top, text="5" ,  command=lambda:calcu(5),height=1, width=4)
button5.grid(row=5, column=2,padx=5,pady=5)

button6 = Button(top, text="6", command=lambda:calcu(6),height=1, width=4)
button6.grid(row=5, column=3,padx=5,pady=5)

button7 = Button(top, text="7", command=lambda:calcu(7),height=1, width=4)
button7.grid(row=4, column=1,padx=5,pady=5)

button3 = Button(top, text="8",  command=lambda:calcu(8),height=1, width=4)
button3.grid(row=4, column=2,padx=5,pady=5)

button3 = Button(top, text="9", command=lambda:calcu(9),height=1, width=4)
button3.grid(row=4, column=3,padx=5,pady=5)

button0 = Button(top, text="0",  command=lambda:calcu(0),height=1, width=4)
button0.grid(row=7, column=2,padx=5,pady=5)

plus= Button(top, text="+" ,  command=lambda:calcu("+"),height=1, width=4)
plus.grid(row=6, column=4,padx=5,pady=5)

minus= Button(top, text="-" , command=lambda:calcu("-"),height=1, width=4)
minus.grid(row=5, column=4,padx=5,pady=5)

mul= Button(top, text="*" ,  command=lambda:calcu("*"),height=1, width=4)
mul.grid(row=4, column=4,padx=5,pady=5)

div= Button(top, text="/" ,  command=lambda:calcu("/"),height=1, width=4)
div.grid(row=7, column=4,padx=5,pady=5)

equals= Button(top, text="=" ,  command=answer,height=1, width=4)
equals.grid(row=7, column=3,padx=5,pady=5)

clear= Button(top, text="c" ,  command=clear,height=1, width=4)
clear.grid(row=7, column=1,padx=5,pady=5)


top.mainloop()
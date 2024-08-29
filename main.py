from tkinter import*
import random
import string


root =Tk()
root.geometry("700x400")
root.title("Password Generator")
root.resizable(False,False)
root.config(bg="white")


passstr = StringVar()
pwd_len = IntVar()

img=PhotoImage(file="bg.png")
Label(root,image=img,bg='white').place(x=2,y=1)

def get_pass():
    pass1 = string.ascii_letters + string.digits +string.punctuation
    password =""

    for x in range (pwd_len.get()):
        password = password + random.choice(pass1)
        passstr.set(password)

Label(root,text="Password Generator",font="Times_New_Roman 20 bold",bg="white").pack()
Label(root,text="Length of Password",fg="navy",bg="white",font=("Helvetica",16)).place(x=435,y=60)
Entry(root,textvariable=pwd_len,width=15,font=("Helvetica",18)).place(x=435,y=100)
Button(root,text="Generate Password",command=get_pass,bg="midnightblue",fg="white",font=("Helvetica",14)).place(x=440,y=160)
Entry(root,textvariable=passstr,width=15,font=("Helvetica",18)).place(x=435,y=230)
Button(root,text="Re-Generate Password",command=get_pass,bg="midnightblue",fg="white",font=("Helvetica",14)).place(x=430,y=300)

root.mainloop()

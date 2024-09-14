from tkinter import *

def mostrar():
    if(x.get()==1):
        print("Acepto")
    else:
        print("No acepto ")


windows =Tk()
windows.geometry('250x300')
windows.title("CheckBox")
windows.iconbitmap('images/Logo-jorge.ico')

#--------------------------------------
x= IntVar()
check_button=Checkbutton(windows, text="Acepto", variable=x, onvalue=1,offvalue=0, command=mostrar )
check_button.place(x=0 , y=10)


windows.mainloop()
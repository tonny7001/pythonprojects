from tkinter import *
#from tkinter import messagebox


#-----------------------------------------------------
#funciones
def click(event):
   label.starX=event.x
   label.starY=event.y

def click2(event):
   x=label.winfo_x()-label.starX +event.x
   y=label.winfo_y()-label.starY +event.y
   label.place(x=x, y=y)

#--------------------------------------------
# interfaz
windows = Tk()
windows.geometry('250x300')
windows.title("Arrastrar widget")
windows.iconbitmap('images/Logo-jorge.ico')
# ---------------------------------------------
label=Label(windows,bg='red',width=10,height=5)
label.place(x=0,y=0)
label.bind("<Button-1>",click)
label.bind("<B1-Motion>",click2)



#-------------------------------------------------
windows.mainloop()
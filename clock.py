import datetime
import time
from tkinter import*
from tkinter import messagebox
import winsound

def alarm():
    x=int(e1.get())
    y=int(e2.get()) 
    messagebox.showinfo("notification","alarm as been set")
    while True:
        if x==datetime.datetime.now().hour and y==datetime.datetime.now().minute:
          for i in range(0,100):
                 winsound.Beep(1000,100)
          break
    
root=Tk()
root.geometry("400x200")
root.title("Alram Clock") 
root.configure(bg='lightgreen')

#Hr
l1=Label(root,text="Hour :",bg='lightgreen',font=('Georgia',15))
l1.grid(row=0,column=0,padx=55,pady=20)

#Min
l2=Label(root,text="Mintues :",bg='lightgreen',font=('Georgia',15)) 
l2.grid(row=1,column=0) 

#entry for Hr 
e1=Entry(root,width=20)
e1.grid(row=0,column=1)

#entry for Min
e2=Entry(root,width=20)
e2.grid(row=1,column=1)

#Button to set alarm
btn=Button(root,text="SET ALARM",fg='black',command=alarm,width=10)
btn.grid(row=2,column=1,pady=10)
root.mainloop()
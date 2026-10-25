from tkinter import *
from datetime import date



root = Tk()
root.title('getting started with wigets')
root.geometry ('400x300')



ibl = Label(text="Hey there!",fg="white",bg="#409789",height=1,width=300)



name_Ibl = Label(text='full name',bg="#ffffff")
name_entry = Entry()

def display():

    name = name_entry.get()

    



    global Message
    Message = "wellcome to the application! \nToday's date is: "
    greet = 'Hello'+name+"\n"


    Text_box.insert(END, greet)
    Text_box.insert(END, Message)
    Text_box.insert(END, date.today())
 

Text_box = Text(height=3)



btn = Button(text="begin",command=display,height=1,bg="#FFFFFF",fg='black')

ibl.pack()
name_Ibl.pack()
name_entry.pack()
btn.pack()
Text_box.pack()

root.mainloop()
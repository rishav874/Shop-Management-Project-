#  modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
 

f=open("Proj_Database",'a+')

root = Tk()
root.title(" ")
root.configure(width=0,height=0,bg="#e3f4f1")
var=-1

# function to add items

def Add_Items():
    global var
    num_lines = 0
    with open("Proj_Database", 'r') as f10:
        for line in f10:
            num_lines += 1
    var=num_lines-1
    E1= Entry_1.get()
    E2=Entry_2.get()
    E3=Entry_3.get()
    E4=Entry_4.get()
    E5=Entry_5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(E1),E2,E3,str(E4),E5))
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    messagebox.showinfo("ADD ITEM", "...ITEM ADDED SUCCESSFULLY...")



# function to delete items

def Delete_Items():
    E1=Entry_1.get()
    with open(r"Proj_Database") as f, open(r"Proj_Database1", "w") as working:
        for line in f:
            if str(E1) not in line:
                working.write(line)
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    os.remove(r"Proj_Database")
    os.rename(r"Proj_Database1", r"Proj_Database")
    messagebox.showinfo("DELETE ITEM", "...ITEM DELETED SUCCESSFULLY...")
    f.close()
    working.close()


def list():
    global var
    var=0
    f.seek(var)
    root_1 = Tk()
    root_1.configure(bg="Gray")
    root_1.title(" Store Database")
    scroll = Scrollbar(root_1)  
    scroll.pack( side = RIGHT, fill = Y)
    My_text = Text(root_1, yscrollcommand = scroll.set ,width=80,height= 50 ,bg= "gray",fg="black", font=("Times", 30))
    string = f.read()
    My_text.insert(END,string)
    My_text.pack( side = LEFT, fill = BOTH )
    scroll.config( command = My_text.yview )




def Clear_Item():
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    Entry_6.delete(0, END)


def Exit():
    Exit= messagebox.askyesno("Exit the System","Do you want to Exit?")
    if Exit > 0:
        root.destroy()
        return


#All labels Entrys Button grid place
Label_0= Label(root,text=" GUPTA GENERAL STORE ",fg="black",font=("Times new roman", 75, 'bold'))
Label_0.grid(columnspan=10)

Label_1=Label(root,text="ENTER ITEM NAME",bg="#e8c1c7",fg="black",bd=8,font=("Times new roman", 30, 'bold'),width=25)
Label_1.grid(row=1,column=0)
Entry_1=Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_1.grid(row=1,column=1)

Label_2=Label(root, text="ENTER ITEM PRICE",height="1",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 30, 'bold'),width=25)
Label_2.grid(row=2,column=0)
Entry_2= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_2.grid(row=2,column=1)

Label_3=Label(root, text="ENTER ITEM QUANTITY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 30, 'bold'),width=25)
Label_3.grid(row=3,column=0)
Entry_3= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_3.grid(row=3,column=1)

Label_4=Label(root, text="ENTER ITEM CATEGORY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 30, 'bold'),width=25)
Label_4.grid(row=4,column=0)
Entry_4= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_4.grid(row=4,column=1)

Label_5=Label(root, text="ENTER ITEM DISCOUNT",bg="#e8c1c7",fg="black",bd=8, font=("Times new roman", 30, 'bold'),width=25)
Label_5.grid(row=5,column=0, padx=10, pady=10)
Entry_5= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_5.grid(row=5,column=1, padx=10, pady=10)


Button_1= Button(root,text="ADD ITEM",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Add_Items)
Button_1.grid(row=6,column=0, padx=10, pady=10)
Button_2= Button(root, text="DELETE ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Delete_Items)
Button_2.grid(row=6,column=1, padx=40, pady=10)
Button_3= Button(root, text="VIEW DATABASE",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=list)
Button_3.grid(row=3,column=3, padx=40, pady=10)
Button_4= Button(root, text="CLEAR SCREEN",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Clear_Item)
Button_4.grid(row=4,column=3, padx=40, pady=10)
Button_5= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=Exit)
Button_5.place(x=850,y=600,height= 102,width=245)
Entry_5= Entry(root, font=("Times new roman", 14),justify='left',bd=8,width=25)
Entry_5.grid(row=1,column=3, padx=10, pady=10)

root.mainloop()

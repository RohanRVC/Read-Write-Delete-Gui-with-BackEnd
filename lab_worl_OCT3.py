from tkinter import *
import tkinter.messagebox as tmsg
import pickle
import os
rvc=Tk()
name=[]
reg=[]
def Read():   
        global name
        global reg
        filename='name.txt'
        filenames='reg.txt'
        if os.path.exists(filename):
            with open(filename,'rb') as f:
                name=pickle.load(f)
        if os.path.exists(filenames):
            with open(filenames,'rb') as f:
                reg=pickle.load(f)
        with open(filename,'wb') as f:
            pickle.dump(name,f)
        with open(filenames,'wb') as f:
            pickle.dump(reg,f)
        with open(filename,'rb')as f:
            name=pickle.load(f)
        with open(filenames,'rb')as f:
            reg=pickle.load(f)
        rss=list(zip(name,reg))
        text.delete(1.0, END)
        text.insert(END,'The books are-:')
        for book in rss:
            text.insert(END, book)
            text.insert(END,',')
def cleararea():
    text.delete(1.0,END)
def Write():
    book=add_Name_value.get()
    reg_noo=add_Reg_no_value.get()
    addName=book.title()
    if add_Name_value.get()=='' or add_Reg_no_value.get()=='' :
            tmsg.showinfo('Details','Kindly Enter Both the values :)')
            return
    else:
        global name
        global reg
        filename='name.txt'
        filenames='reg.txt'
        if os.path.exists(filename):
            print("ghus gaya")
            with open(filename,'rb') as f:
                name=pickle.load(f)
        if os.path.exists(filenames):
            with open(filenames,'rb') as f:
                reg=pickle.load(f) 
        name.append(addName)
        reg.append(reg_noo)
        with open(filename,'wb') as f:
            pickle.dump(name,f)
        with open(filenames,'wb') as f:
            pickle.dump(reg,f)
        with open(filename,'rb')as f:
            name=pickle.load(f)
        with open(filenames,'rb')as f:
            reg=pickle.load(f)
        text.delete(1.0, END)
        text.insert(END,f'Inserted the name {addName} and its register numberr is {reg_noo} .')     
        return
def Delete():
        global name
        global reg
        filename='name.txt'
        filenames='reg.txt'
        if os.path.exists(filename):
            print("ghus gaya")
            with open(filename,'rb') as f:
                name=pickle.load(f)
        if os.path.exists(filenames):
            with open(filenames,'rb') as f:
                reg=pickle.load(f)
        name.pop()
        reg.pop()
        with open(filename,'wb') as f:
            pickle.dump(name,f)
        with open(filenames,'wb') as f:
            pickle.dump(reg,f)
        with open(filename,'rb')as f:
            name=pickle.load(f)
        with open(filenames,'rb')as f:
            reg=pickle.load(f)
        text.delete(1.0, END)
        text.insert(END,f'Deleted last item name .')
rvc.geometry("1000x644")
rvc.minsize(1000,644)
rvc.maxsize(1000,644)
Label(text="CRUD operations in Databases ",font="algerian 30 bold",fg='grey').grid(row=1,column=2)
Button(text="Read-:",command=Read,padx=20,pady=10).grid(row=2,column=1,padx=11,pady=5)
Button(text="Write-:",command=Write,padx=20,pady=10).grid(row=2,column=2,padx=11,pady=5)
Button(text="Delete Last item -:",command=Delete,padx=20,pady=10).grid(row=2,column=4,padx=11,pady=5)
add_Name=Label(text="Enter Name").grid(row=3,column=1)
add_Reg_no=Label(text="Enter Register no-:").grid(row=4,column=1)
add_Name_value=StringVar()
add_Reg_no_value=StringVar()
add_Name_entry=Entry(rvc,textvariable=add_Name_value).grid(row=3,column=2)
add_Reg_no_entry=Entry(rvc,textvariable=add_Reg_no_value).grid(row=4,column=2)
Label(text="TEXT DISPLAY ",font="algerian 20 bold",fg='grey').grid(row=5,column=2)
text=Text(rvc, width=80, height=20)
text.grid(row=8,column=2)
Button(text="Clear",command=cleararea,padx=15,pady=5).grid(row=6,column=1,padx=11,pady=5)
Button(text="EXIT",command=quit,padx=15,pady=5).grid(row=6,column=4,padx=11,pady=5)
rvc.mainloop()
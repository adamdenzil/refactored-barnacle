from tkinter import *
root=Tk() 
root.title("Try and except") 
root.geometry("500x500")
 
list_name1 = ["micky mouse","tom and jerry","Ben 10","doramon"]
Dict_name={"name":"Adam",
           "age": "12"}


try:
   print(list_name1[5])
   print(Dict_name["Grade"])
except IndexError:   
  messagebox.showinfo("error","this index doesn't exist")
  
except KeyError:
    messagebox.showinfo("error","this Key doesn't exist")
mainloop()
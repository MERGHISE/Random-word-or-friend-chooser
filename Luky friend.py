# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:40:53 2022

@author: ashvi
"""

from tkinter import *
import random

root=Tk()
 
root.title("List")
root.geometry("500x500")



Label1 = Label(root)
Label2 = Label(root)

 
List1 = ["Bottle","Tiffin","ID Card","Chocolates","Chips","Tickets","Hanky"] 
Label1["text"] = "Listed_items : " + str(List1)
def addfriend():
   random_list = random.sample(range(0,7),1) 
   Label2["text"] = "Put Item no " + str(random_list) + " In bag" 
Label1.place(relx=0.5,rely = 0.4, anchor = CENTER) 
    
btn = Button(root, text="Add to the friendlist", command = addfriend)
btn.place(relx= 0.5,rely = 0.3, anchor = CENTER)

Label1.place(relx= 0.5,rely = 0.4, anchor = CENTER )



Label2.place(relx= 0.5,rely = 0.6, anchor = CENTER)


root.mainloop()




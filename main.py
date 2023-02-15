from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('To Do')
# root.iconbitmap('')
root.geometry("500x500")

td_font = Font(
    family = "Arial Rounded MT Bold",
    size= 30
    )

frame = Frame(root)
frame.pack(pady=10)

td_listbox = Listbox(frame, 
                  font = td_font,
                  width = 25,
                  height = 5,
                  bg = "SystemButtonFace",
                  bd = 0,
                  fg="#464646",
                  highlightthickness = 0,
                  selectbackground = "#a6a6a6",
                  activestyle = "none"
                  )

td_listbox.pack(side = LEFT, fill = BOTH)

list_content = ["Eat",
                "Code"
                "Sleep", 
                "Repeat"
                ]

for item in list_content:
    td_listbox.insert(END, item)
    

td_scrollbar = Scrollbar(frame)
td_scrollbar.pack(side = RIGHT, fill = BOTH)

td_listbox.config(yscrollcommand = td_scrollbar.set)
td_scrollbar.config(command = td_listbox.yview)

td_entrybox = Entry(root, font = ("Helvetica"))
td_entrybox.pack(pady = 20)

btn_frame = Frame(root)
btn_frame.pack(pady = 20)

def deleteItem():
    td_listbox.delete(ANCHOR)

def addItem():
    pass

def selectItem():
    pass

def unselectItem():
    pass

delete_btn = Button(btn_frame, text = "DELETE", command = deleteItem)
add_btn = Button(btn_frame, text = "ADD", command = addItem)
select_btn = Button(btn_frame, text = "SELECT", command = selectItem)
unselect_btn = Button(btn_frame, text = "UNSELECT", command = unselectItem)

delete_btn.grid(row = 0, column = 0)
add_btn.grid(row = 0, column = 1, padx = 20)
select_btn.grid(row = 0, column = 2, padx = 20)
unselect_btn.grid(row = 0, column = 3, padx = 20)

root.mainloop()
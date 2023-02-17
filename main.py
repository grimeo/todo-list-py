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


list_content = ["Code",
                "Eat",
                "Sleep", 
                "Repeat"
                ]

for item in list_content:
    td_listbox.insert(END, item)
    

td_scrollbar = Scrollbar(frame)
td_scrollbar.pack(side = RIGHT, fill = BOTH)

td_listbox.config(yscrollcommand = td_scrollbar.set)
td_scrollbar.config(command = td_listbox.yview)

td_listbox.pack(side = LEFT, fill = BOTH)

td_entrybox = Entry(root, font = ("Helvetica"))
td_entrybox.pack(pady = 20)

btn_frame = Frame(root)
btn_frame.pack(pady = 20)

def deleteItem():
    td_listbox.delete(ANCHOR)

def addItem():
    td_listbox.insert(END, td_entrybox.get())
    td_entrybox.delete(0, END)

def selectItem():
    td_listbox.itemconfig(
        td_listbox.curselection(),
        fg="#dedede"
    )
    td_listbox.select_clear(0,END)
    
def unselectItem():
    td_listbox.itemconfig(
        td_listbox.curselection(),
        fg="#464646"
    )
    td_listbox.select_clear(0,END)
    
def deleteSelected():
    count = 0
    while count < td_listbox.size():
        if td_listbox.itemcget(count, "fg") == "#dedede":
            td_listbox.delete(td_listbox.index(count))
        
        count += 1
        
        

delete_btn = Button(btn_frame, text = "DELETE", command = deleteItem)
add_btn = Button(btn_frame, text = "ADD", command = addItem)
select_btn = Button(btn_frame, text = "SELECT", command = selectItem)
unselect_btn = Button(btn_frame, text = "UNSELECT", command = unselectItem)
delete_selected_btn = Button(btn_frame, text = "DELETE SELECTED", command = deleteSelected)

delete_btn.grid(row = 0, column = 0)
add_btn.grid(row = 0, column = 1, padx = 20)
select_btn.grid(row = 0, column = 2, padx = 20)
unselect_btn.grid(row = 0, column = 3, padx = 20)
delete_selected_btn.grid(row = 0, column = 4)

root.mainloop()
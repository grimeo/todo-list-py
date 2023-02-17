from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

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


list_content = [
                "Eat",
                "Sleep", 
                "Repeat",
                "Code"
                ]

for item in list_content:
    td_listbox.insert(END, item)
    

td_scrollbar = Scrollbar(frame)
td_scrollbar.pack(side = RIGHT, fill = BOTH)

td_listbox.config(yscrollcommand = td_scrollbar.set)
td_scrollbar.config(command = td_listbox.yview)

td_listbox.pack(side = LEFT, fill = BOTH)

td_entrybox = Entry(root, font = ("Arial Rounded MT Bold", 24), width = 26)
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
        
        else:
            count += 1
        

def saveList():
    td_file_name = filedialog.asksaveasfilename(
        initialdir = "C:\\Users\\Flynn\\Desktop\\3Y-1S\\DSA\\todo-finals",
        title = "Save File",
        filetypes = (
            ("Dat Files","*.dat"), 
            ("All Files", "*.*")
            )
        )
    if td_file_name:
        if td_file_name.endswith(".dat"):
            pass
        else:
            td_file_name = f'{td_file_name}.dat'
        
        count = 0
        while count < td_listbox.size():
            if td_listbox.itemcget(count, "fg") == "#dedede":
                td_listbox.delete(td_listbox.index(count))
            
            else:
                count += 1
                
        list = td_listbox.get(0, END)
        
        td_output_file = open(td_file_name, 'wb')
        
        pickle.dump(list, td_output_file)

def openList():
    td_file_name = filedialog.askopenfilename(
        initialdir = "C:\\Users\\Flynn\\Desktop\\3Y-1S\\DSA\\todo-finals",
        title = "Open File",
        filetypes = (
            ("Dat Files","*.dat"), 
            ("All Files", "*.*")
            )
        )     
    if td_file_name:
        td_listbox.delete(0, END)
        
        td_input_file = open(td_file_name, 'rb')
        
        list = pickle.load(td_input_file)
        
        for item in list:
            td_listbox.insert(END, item)

def clearList():
    td_listbox.delete(0,END)
    
def sortAscending():
    tdList = list(td_listbox.get(0, END))
    tdList = sorAsctList(tdList)
    td_listbox.delete(0,END)
    for item in tdList:
        td_listbox.insert(END, item)
    
def sortDescending():
    tdList = list(td_listbox.get(0, END))
    tdList = sorDestList(tdList)
    td_listbox.delete(0,END)
    for item in tdList:
        td_listbox.insert(END, item)

def sorAsctList(array):
    greaterElems = []
    lesserElems = []
    arrlen = len(array)
    if arrlen <= 1:
        return array
    else:
        pivot = array.pop()
    for element in array:
        if element > pivot:
            greaterElems.append(element)
        else:
            lesserElems.append(element)
    return sorAsctList(lesserElems) + [pivot] + sorAsctList(greaterElems)

def sorDestList(array):
    greaterElems = []
    lesserElems = []
    arrlen = len(array)
    if arrlen <= 1:
        return array
    else:
        pivot = array.pop()
    for element in array:
        if element < pivot:
            greaterElems.append(element)
        else:
            lesserElems.append(element)
    return sorDestList(lesserElems) + [pivot] + sorDestList(greaterElems)


td_menu = Menu(root)
root.config(menu = td_menu)

td_file_menu = Menu(td_menu, tearoff = False)
td_menu.add_cascade(label = "File", menu = td_file_menu)

td_file_menu.add_command(label="Save List", command = saveList)
td_file_menu.add_command(label="Open List", command = openList)
td_file_menu.add_separator()
td_file_menu.add_command(label="Clear List", command = clearList)

delete_btn = Button(btn_frame, text = "DELETE", command = deleteItem)
add_btn = Button(btn_frame, text = "ADD", command = addItem)
select_btn = Button(btn_frame, text = "SELECT", command = selectItem)
unselect_btn = Button(btn_frame, text = "UNSELECT", command = unselectItem)
delete_selected_btn = Button(btn_frame, text = "DELETE SELECTED", command = deleteSelected)
sort_asc_btn = Button(btn_frame, text = "Sort Ascending", command = sortAscending)
sort_des_btn = Button(btn_frame, text = "Sort Descending", command = sortDescending)


delete_btn.grid(row = 0, column = 0)
add_btn.grid(row = 0, column = 1, padx = 20)
select_btn.grid(row = 0, column = 2, padx = 20)
unselect_btn.grid(row = 0, column = 3, padx = 20)
delete_selected_btn.grid(row = 0, column = 4)
sort_asc_btn.grid(row = 1, column = 1, pady = 20    )
sort_des_btn.grid(row = 1, column = 2, padx = 20)


root.mainloop()
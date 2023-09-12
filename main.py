import tkinter
from tkinter import Scrollbar, VERTICAL
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror, showinfo

FILE_NAME = tkinter.NONE
BYTE_NUMBERS_ARRAY = [0]
POINTER = -1
INP = None


def new_file(*args):
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)


def save_file(*args):
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as(*args):
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")


def open_file(*args):
    global FILE_NAME
    global INP
    global BYTE_NUMBERS_ARRAY
    global POINTER
    INP = askopenfile(mode="r")
    if INP is None:
        return
    FILE_NAME = INP.name
    text.delete('1.0', tkinter.END)
    for i in range(5):
        data = INP.readline()
        text.insert(tkinter.END, data)
    BYTE_NUMBERS_ARRAY.append(INP.tell())
    POINTER += 1


def next_portion(*args):
    global FILE_NAME
    global BYTE_NUMBERS_ARRAY
    global INP
    global POINTER
    if FILE_NAME is tkinter.NONE:
        return
    text.delete('1.0', tkinter.END)
    for i in range(5):
        data = INP.readline()
        text.insert(tkinter.END, data)
    if POINTER == len(BYTE_NUMBERS_ARRAY) and INP.tell() != BYTE_NUMBERS_ARRAY[-1]:
        BYTE_NUMBERS_ARRAY.append(INP.tell())
    if INP.tell() != BYTE_NUMBERS_ARRAY[-1]:
        POINTER += 1


def prev_portion(*args):
    global FILE_NAME
    global BYTE_NUMBERS_ARRAY
    global INP
    global POINTER
    if FILE_NAME is tkinter.NONE or POINTER == 0:
        return
    text.delete('1.0', tkinter.END)
    INP.seek(BYTE_NUMBERS_ARRAY[POINTER - 1])
    for i in range(5):
        data = INP.readline()
        text.insert(tkinter.END, data)
    POINTER -= 1


def info():
    showinfo("Information", "Text Editor")


def copy_text():
    selected_text = text.selection_get()
    if selected_text:
        text.clipboard_clear()
        text.clipboard_append(selected_text)


def cut_text():
    selected_text = text.selection_get()
    if selected_text:
        text.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.clipboard_clear()
        text.clipboard_append(selected_text)


def paste_text():
    clipboard_text = text.clipboard_get()
    if clipboard_text:
        text.insert(tkinter.INSERT, clipboard_text)
    text.update()


root = tkinter.Tk()
root.title("CDL Notepad v.0.1")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word")
scroll_bar = Scrollbar(root, orient=VERTICAL, command=text.yview)
scroll_bar.pack(side="right", fill="y")
text.configure(yscrollcommand=scroll_bar.set)

text.pack()
menu_bar = tkinter.Menu(root)

file_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
root.bind("<Control-n>", new_file)
file_menu.add_command(label="Open", command=open_file)
root.bind("<Control-o>", open_file)
file_menu.add_command(label="Save", command=save_file)
root.bind("<Control-s>", save_file)
file_menu.add_command(label="Save as", command=save_as)
root.bind("<Alt-s>", save_as)

edit_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Cut", command=cut_text)

menu_bar.add_cascade(label="Info", command=info)

menu_bar.add_cascade(label="Next portion", command=next_portion)
root.bind("<Alt-m>", next_portion)

menu_bar.add_cascade(label="Previous portion", command=prev_portion)
root.bind("<Alt-b>", prev_portion)

root.config(menu=menu_bar)
root.mainloop()

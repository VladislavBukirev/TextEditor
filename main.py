import tkinter
from tkinter import Scrollbar, VERTICAL
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror, showinfo

FILE_NAME = tkinter.NONE


def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)


def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as():
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)


def info():
    showinfo("Information", "Text Editor")


def copy_text():
    selected_text = text.selection_get()
    if selected_text:
        text.clipboard_clear()
        text.clipboard_append(selected_text)


def paste_text():
    text.clipboard_append(text.clipboard_get())
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
menuBar = tkinter.Menu(root)

fileMenu = tkinter.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)
menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = tkinter.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Copy", command=copy_text)
editMenu.add_command(label="Paste", command=paste_text)
menuBar.add_cascade(label="Edit", menu=editMenu)

menuBar.add_cascade(label="Info", command=info)

root.config(menu=menuBar)
root.mainloop()

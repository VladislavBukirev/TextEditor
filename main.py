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


def cut_text():
    selected_text = text.selection_get()
    if selected_text:
        text.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.clipboard_clear()
        text.clipboard_append(selected_text)


root = tkinter.Tk()
root.title("Text editor")

root.minsize(width=400, height=400)
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
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as)

edit_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Cut", command=cut_text)

menu_bar.add_cascade(label="Info", command=info)

menu_bar.add_cascade(label="Exit", command=root.quit)

root.config(menu=menu_bar)
root.mainloop()

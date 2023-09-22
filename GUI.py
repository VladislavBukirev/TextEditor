import tkinter
from tkinter import Scrollbar, VERTICAL
import TextEditor


def new_file():
    text.delete('1.0', tkinter.END)
    TextEditor.new_file()


def save_as():
    TextEditor.save_as(data=text.get('1.0', tkinter.END))


def save():
    TextEditor.save_file(data=text.get('1.0', tkinter.END))


def open_file(file=None):
    text.delete('1.0', tkinter.END)
    for data in TextEditor.open_file(None, file):
        text.insert(tkinter.END, data)


def next_portion():
    TextEditor.save_portion(text.get('1.0', 'end-1c'))
    text.delete('1.0', tkinter.END)
    for data in TextEditor.next_portion():
        text.insert(tkinter.END, data)


def prev_portion():
    TextEditor.save_portion(text.get('1.0', 'end-1c'))
    text.delete('1.0', tkinter.END)
    for data in TextEditor.prev_portion():
        text.insert(tkinter.END, data)


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
root.bind("<Control-n>", TextEditor.new_file)
file_menu.add_command(label="Open", command=open_file)
root.bind("<Control-o>", TextEditor.open_file)
file_menu.add_command(label="Save", command=save)
root.bind("<Control-s>", TextEditor.save_file)
file_menu.add_command(label="Save as", command=save_as)
root.bind("<Alt-s>", TextEditor.save_as)

edit_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Cut", command=cut_text)

menu_bar.add_cascade(label="Info", command=TextEditor.info)

menu_bar.add_cascade(label="Next portion", command=next_portion)
root.bind("<Alt-m>", TextEditor.next_portion)

menu_bar.add_cascade(label="Previous portion", command=prev_portion)
root.bind("<Alt-b>", TextEditor.prev_portion)

root.config(menu=menu_bar)

if __name__ == '__main__':
    root.mainloop()
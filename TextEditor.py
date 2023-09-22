import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror, showinfo

FILE_NAME = tkinter.NONE
BYTE_NUMBERS_ARRAY = [0]
POINTER = -1
INP = None
CONTENT = ""


def new_file(*args):
    global FILE_NAME
    FILE_NAME = "Untitled"


def save_file(*args, data):
    try:
        out = open(FILE_NAME, 'w')
    except FileNotFoundError:
        out = open(FILE_NAME, 'x')
    out.write(data)
    out.close()


def save_as(*args, data):
    out = asksaveasfile(mode='w', defaultextension='txt')
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")


def open_file(caller, file=None):
    global FILE_NAME
    global INP
    global BYTE_NUMBERS_ARRAY
    global POINTER
    if file is None:
        INP = askopenfile(mode="r+")
    else:
        INP = open(file, mode="r+")
    if INP is None:
        return
    FILE_NAME = INP.name
    for i in range(5):
        yield INP.readline()
    BYTE_NUMBERS_ARRAY.append(INP.tell())
    POINTER += 1


def next_portion(*args):
    global BYTE_NUMBERS_ARRAY
    global INP
    global POINTER
    if INP.name is tkinter.NONE:
        return
    for i in range(5):
        yield INP.readline()
    if INP.tell() != BYTE_NUMBERS_ARRAY[-1]:
        if POINTER == len(BYTE_NUMBERS_ARRAY) - 2:
            BYTE_NUMBERS_ARRAY.append(INP.tell())
        else:
            BYTE_NUMBERS_ARRAY[POINTER + 1] = INP.tell()
        POINTER += 1


def prev_portion(*args):
    global BYTE_NUMBERS_ARRAY
    global INP
    global POINTER
    if INP.name is tkinter.NONE or POINTER == 0:
        return
    INP.seek(BYTE_NUMBERS_ARRAY[POINTER - 1])
    for i in range(5):
        yield INP.readline()
    POINTER -= 1


def save_portion(content):
    global BYTE_NUMBERS_ARRAY
    global POINTER
    global INP
    file = open(INP.name, 'r+')
    file.seek(BYTE_NUMBERS_ARRAY[POINTER])

    if POINTER != len(BYTE_NUMBERS_ARRAY) - 1:
        BYTE_NUMBERS_ARRAY[POINTER + 1] = BYTE_NUMBERS_ARRAY[POINTER] + file.write(content) + 5
    else:
        BYTE_NUMBERS_ARRAY.append(BYTE_NUMBERS_ARRAY[POINTER] + file.write(content) + 5)
    file.close()


def info():
    showinfo("Information", "Text Editor")
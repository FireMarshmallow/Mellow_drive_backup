import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

root = Tk()
root.title("mellow mirror backup V1.0 beta")
path = "."
global Source_drive
global Destination_drive


def folder1():
    global Source_drive
    Source_drive = filedialog.askdirectory()


def folder2():
    global Destination_drive
    Destination_drive = filedialog.askdirectory()


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
                print('copying: ', s, 'to: ', d)


def changeText1():
    Button1['text'] = Source_drive


def changeText2():
    Button2['text'] = Destination_drive


Button1 = tk.Button(root, text="Source_drive", height=5,
                    width=50, command=lambda: [folder1(), changeText1()])
Button2 = tk.Button(root, text="Destination_drive", height=5,
                    width=50, command=lambda: [folder2(), changeText2()])

Button3 = tk.Button(root, text="Start backup", height=5, width=50, command=lambda: [
                    copytree(Source_drive, Destination_drive)])

Button1.pack()
Button2.pack()
Button3.pack()
root.mainloop()

import os
import pickle
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import sys
import time

import datetime

root = Tk()
root.title("mellow mirror backup V2.0 beta")
path = "."
global Source_drive
global Destination_drive


def folder1():
    global Source_drive
    Source_drive = filedialog.askdirectory()


def folder2():
    global Destination_drive
    Destination_drive = filedialog.askdirectory()


def do_it():
    copytree(Source_drive, Destination_drive)
    copytree(Destination_drive, Source_drive)


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

    Save(Source_drive, Destination_drive, datatosave)
    print('Dane')

# save


def save_file_path():
    PathAndName = os.path.join(sys.path[0], "mellow_Backup_save.dat")
    return PathAndName


def Save(Source_drive, Destination_drive, datatosave):
    thing_to_save_for_next_time = []
    thing_to_save_for_next_time.clear()
    thing_to_save_for_next_time = [
        Source_drive,
        Destination_drive,
        datatosave,
    ]
    outfile = open(save_file_path(), "wb")
    pickle.dump(thing_to_save_for_next_time, outfile)
    outfile.close()


datatosave = datetime.datetime.now()


def open_save():
    try:
        infile = open(save_file_path(), "rb")
        new_dict = pickle.load(infile)
        infile.close()
        global Destination_drive
        global Source_drive
        global last_backup
        Source_drive = new_dict[0]
        Destination_drive = new_dict[1]
        last_backup = new_dict[2]
        changeText1()
        changeText2()
        changeText3()
    except:
        pass

# save end


def changeText1():
    Button1['text'] = Source_drive


def changeText2():
    Button2['text'] = Destination_drive


def changeText3():
    f_date = last_backup
    l_date = datetime.datetime.now()
    delta = l_date - f_date
    last = 'days sins last backup: ' + str(delta.days)
    last_save_lub['text'] = last


last_save_lub = tk.Label(root, text="days sins last backup: N/A")

Button1 = tk.Button(root, text="Source_drive", height=5,
                    width=50, command=lambda: [folder1(), changeText1()])
Button2 = tk.Button(root, text="Destination_drive", height=5,
                    width=50, command=lambda: [folder2(), changeText2()])

Button3 = tk.Button(root, text="Start backup",
                    height=5, width=50, command=do_it)
Button0 = tk.Button(root, text="Save", activeforeground="blue",
                    height=5, width=20, command=lambda: [Save(Source_drive, Destination_drive, datatosave)])

last_save_lub.pack()
Button1.pack()
Button2.pack()
Button3.pack()
Button0.pack()

open_save()
root.mainloop()

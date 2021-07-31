from tkinter import *
from tkinter.ttk import *
import sqlite3
import cv2
import numpy as np
import os
from PIL import Image
from tkinter import messagebox
import tkinter
import tkinter as tk

window = tk.Tk()
window.title("Face Recognition system")


l1 = tk.Label(window, text="Name", font=("Times New Roman",16))
l1.grid(column=0, row=0)
t1 = tk.Entry(window, width=30, )
t1.grid(column=1, row=0)

l2 = tk.Label(window, text="Age", font=("Times New Roman",16))
l2.grid(column=0, row=1)
t2 = tk.Entry(window, width=30, )
t2.grid(column=1, row=1)

l3 = tk.Label(window, text="Address", font=("Times New Roman",16))
l3.grid(column=0, row=2)
t3 = tk.Entry(window, width=30, )
t3.grid(column=1, row=2)


b1 = tk.Button(window, text="Training", font=("Times New Roman",14),bg="black",fg="red",width = 13 )
b1.grid(column=4, row=6)

b2 = tk.Button(window, text="get information", font=("Times New Roman",14), bg="black", fg="red", width = 13)
b2.grid(column=5, row=6)

b3 = tk.Button(window, text="identity check", font=("Times New Roman",14), bg="black", fg="red", width = 13)
b3.grid(column=6, row=6)

window.geometry("800x400")

window.mainloop()
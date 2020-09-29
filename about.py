from tkinter import *
import os

def getAbout():
    top = Tk()
    top.geometry("420x320")
    top.title("About")
    top.iconbitmap("icons/quest.ico")
    top.config(bg="#303030")
    top.resizable(height=False, width=False)
    num = 0

    with open("about.txt", "r") as about:
        for line in about:
            num += 1
            lbl = Label(top, text=line, font=("Roboto", 11), bg="#303030", fg="#fff")
            lbl.pack()





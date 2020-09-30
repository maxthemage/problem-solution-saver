from tkinter import *
from tkinter import messagebox
import datetime
import os, csv
import about as abt

directory = os.path.dirname(os.path.realpath(__file__))
files = "assests"
path = os.path.join(directory, files)
main_file = "solutions.csv"
date = datetime.datetime.now()
date = (date.strftime("%a, %b %d %Y at %I:%M%p"))

#Help me :)
def addProb():
    prob = probEnt.get()
    sol = solEnt.get()
    if not os.path.exists(path):
        if (not (len(sol) ==0)) and (not (len(prob) == 0)):
            os.mkdir(path)
            os.chdir(path)
            with open(main_file, "w") as file:
                writer = csv.writer(file)
                writer.writerow(["Problem", "Solution", "Date logged"])
                writer.writerow([prob.title(), sol, date])
                messagebox.showinfo("Prolution", "Problem and Solution were added")
        else:
            messagebox.showerror("Error", "Input fields empty! Cannot add empty fields.")
    else:
        os.chdir(path)
        if (len(solEnt.get()) == 0) or (len(probEnt.get()) == 0):
            messagebox.showerror("Error", "Input fields empty! Cannot add empty fields.")
        else:
            if not os.path.exists(main_file):
                with open(main_file, "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Problem", "Solution", "Date logged"])
                    writer.writerow([prob.title(), sol, date])
                    messagebox.showinfo("Prolution", "Problem and Solution were added")
            elif os.path.getsize(main_file) == 0:
                with open(main_file, "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Problem", "Solution", "Date logged"])
                    writer.writerow([prob.title(), sol, date])
                    messagebox.showinfo("Prolution", "Problem and Solution were added")
            else:
                with open(main_file, "a") as file:
                    writer = csv.writer(file)
                    writer.writerow([prob.title(), sol, date])
                    messagebox.showinfo("Prolution", "Problem and Solution were added")

def viewAll():
    if os.path.exists(path):
        os.chdir(path)
        os.startfile(main_file)
    else:
        messagebox.showerror("Error", "No problems saved yet")

def delAll():
    ans = messagebox.askokcancel("Prolution", "All your items will be deleted. Are you sure you want to continue?")
    if ans == 1:
        if not os.path.exists(path):
            messagebox.showerror("Error", "No items exists")
        else:
            os.chdir(path)
            with open(main_file, "w") as file:
                writer = csv.writer(file)
                writer.writerow("")
    else:
        pass
    
root = Tk()
root.title("Prolution")
root.geometry("515x255")
root.resizable(width=False, height=False)
root.iconbitmap("icons/quest.ico")
root.config(bg="#303030")

mainMenu = Menu(root)
root.config(menu=mainMenu)
options = Menu(mainMenu)
about = Menu(mainMenu)

mainMenu.add_cascade(label="Options", menu=options)
mainMenu.add_cascade(label="About", menu=about)
options.add_command(label="View...", command=viewAll)
options.add_command(label="Search..", state=DISABLED)
options.add_command(label="Delete all..", command=delAll)
about.add_command(label="...", command=abt.getAbout)

padone = Label(root, text="", bg="#303030", pady=1)
padTwo = Label(root, text="", bg="#303030")
header = Label(root, text = "Store and manage your coding problems", fg="#00cccc", bg="#303030", font=("Impact", 22), padx=10,)
header2 = Label(root, text = "and solutions", fg="#00cccc", bg="#303030", font=("Impact", 22), padx=10)
proHeading = Label(root, text = "Enter problem:", fg="#fff", bg="#303030", font=("Georgia", 15))
probEnt = Entry(root, width=44, font=("Roboto", 11))
solHeading = Label(root, text = "Enter solution:", fg="#fff", bg="#303030",font=("Georgia", 15))
solEnt =Entry(root, width=44, font=("Roboto", 11))
btn = Button(root, text="submit", fg="#303030", bg="#00cccc", font=("Impact", 10), padx=2, pady=2, command=addProb)

header.grid(columnspan=2, row=0)
header2.grid(columnspan=2, row=1)
padTwo.grid(columnspan=2, row=2)
proHeading.grid(columnspan=1, row=3)
probEnt.grid(column=1, row=3)
solHeading.grid(columnspan=1, row=4)
solEnt.grid(column=1, row=4)
padone.grid(column=1, row=5)
btn.grid(columnspan=2, row=6)



root.mainloop()

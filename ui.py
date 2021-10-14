from tkinter import *
from tkinter.ttk import *

def title_page():
    print("title page")

def study_bank():
    print("study bank")

def class_schedule():
    print("class schedule")

def zoom_login():
    print("zoom login")

root=Tk()

root.geometry('600x600')

# buttons
b_title_page = Button(root, text = "Create Title Page", command = title_page)
b_study_bank = Button(root, text = "Create Study Bank", command = study_bank)
b_class_schedule = Button(root, text = "Show Class Schedule", command = class_schedule)
b_zoom_login = Button(root, text = "Show Class Schedule", command = zoom_login)

# button grid assignment
b_title_page.grid(row = 0, column = 0, sticky = W, pady = 2)
b_study_bank.grid(row = 1, column = 0, sticky = W, pady = 2)
b_class_schedule.grid(row = 2, column = 0, sticky = W, pady = 2)
b_zoom_login.grid(row = 3, column = 0, sticky = W, pady = 2)




root.mainloop()
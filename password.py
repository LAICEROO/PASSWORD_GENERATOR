from tkinter import *
from random import randint

root = Tk()
root.title('Strong password generator')
root.geometry("500x300")

my_password = chr(randint(33, 126))

def new_rand():
    pass

def copy():
    pass

# Label frame
labelF = LabelFrame(root, text=("How many characters?"))
labelF.pack(pady=20)

# Create entry box to degignate number of characters
my_entry = Entry(labelF, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create entry box for our returned password
pass_entry = Entry(root, text='', font=("Helvetica, 24"))
pass_entry.pack(pady=20)

# Create a frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

copy_button = Button(my_frame, text="Copy", command=copy)
copy_button.grid(row=0, column=1, padx=10)



root.mainloop()
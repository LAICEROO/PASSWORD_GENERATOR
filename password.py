from tkinter import *
from random import randint

root = Tk()
root.title('Strong password generator')
root.geometry("500x300")

my_password = chr(randint(33, 126))

# Label frame
labelF = LabelFrame(root, text="How many characters?")
labelF.pack(pady=20)

# Create entry box to degignate number of characters
my_entry = Entry(labelF, font=("Sans Serif", 24))
my_entry.pack(pady=20, padx=20)

# Create entry box for our returned password

root.mainloop()
from tkinter import *
from random import randint


root = Tk()
root.title('Strong password generator')
root.geometry("500x300")

my_password = chr(randint(33, 126))

# Generate random strong password
def new_rand():
    # Clear out entry box
    pass_entry.delete(0, END)
    
    # Get password length and convert to integer
    pass_length = int(my_entry.get())

    # Create a variable to hold password
    my_password = ''

    # Loop through password length
    for x in range(pass_length):
        my_password += chr(randint(33, 126))

    # Output password to the screen
    pass_entry.insert(0, my_password)

# Copy to clipboard
def copy():
    # Clear the clipboard
    root.clipboard_clear()

    # Copy to clipboard
    root.clipboard_append(pass_entry.get())


# Label frame
labelF = LabelFrame(root, text=("How many characters?"))
labelF.pack(pady=20)

# Create entry box to degignate number of characters
my_entry = Entry(labelF, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create entry box for our returned password
pass_entry = Entry(root, text='', font=("Helvetica, 24"), bd=0, bg="systembuttonface") 
pass_entry.pack(pady=20)

# Create a frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

copy_button = Button(my_frame, text="Copy password", command=copy)
copy_button.grid(row=0, column=1, padx=10)



root.mainloop()
# Practice creating buttons

from tkinter import *


def callback():
    print("YOU CLICKED ME!")

button = Button(text="Click Me!", command=callback)
button.pack() # Display the button

mainloop()


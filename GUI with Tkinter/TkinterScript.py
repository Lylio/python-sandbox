from tkinter import *

# Create window and title
window = Tk()
window.title("Miles to Km Convertor")


# Function to convert miles to kilometers
def km_to_miles():
    miles = float(e1_value.get()) * 1.61
    t1.insert(END, miles)


# Creation and placement of 'Miles' label
labelMiles = Label(window, text="Miles")
labelMiles.grid(row=0, column=0)

# Creation and placement of 'Km' label
labelKm = Label(window, text="Km")
labelKm.grid(row=0, column=2)

# Adding spacing on 2nd row
window.grid_rowconfigure(1, minsize=50)

# Creation and placement of 'Convert' button
b1 = Button(window, text="Convert", command=km_to_miles)
b1.grid(row=1, column=2)

# Creation and placement of miles entry field
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Creation and placement of km text field
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=3)

# mainloop() basically keeps the window running until destroyed
window.mainloop()

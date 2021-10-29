from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Window
window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()


# Entry
input = Entry(width=65)
print(input.get())
input.pack()

window.mainloop()

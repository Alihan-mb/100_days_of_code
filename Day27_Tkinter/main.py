import tkinter

window = tkinter.Tk()

i = 0
def button_clicked():
    global i
    i += 1
    print("I got clicked")
    my_label["text"] = "The button was clicked"
    if i >= 2:
        my_label["text"] = entry.get()


window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
# Entry
entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)


new_button = tkinter.Button(text="I run the code")
new_button.grid(column=2, row=0)


window.mainloop()

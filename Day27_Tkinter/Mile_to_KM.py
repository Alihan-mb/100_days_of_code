import tkinter

window = tkinter.Tk()
window.title("Mile to KM converter")

window.config(padx=50, pady=50)
# window.configure(background="white")


entry = tkinter.Entry(width=15)
entry.insert(string="0", index=0)
entry.grid(column=1, row=0)

def converting_miles_to_km():
    km_number = float(entry.get())
    formula = km_number * 1.609
    converted_value["text"] = round(formula)


convert_label = tkinter.Label(text="is equal to")
convert_label.grid(column=0, row=1)
convert_label.config(height=1, width=10)

converted_value = tkinter.Label(text=0)
converted_value.grid(column=1, row=1)
converted_value.config(height=1, width=10)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(height=1, width=10)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(height=1, width=10)

calculate_button = tkinter.Button(text="Calculate", command=converting_miles_to_km)
calculate_button.config(height=1, width=10)
calculate_button.grid(column=1, row=2)


window.mainloop()

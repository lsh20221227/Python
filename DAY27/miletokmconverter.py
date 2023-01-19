import tkinter

def button_click():
     miles = int(input.get())
     km = 1.60934 * miles
     label_result.config(text=f"{km}") # CHECK

window = tkinter.Tk()
window.minsize()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20, background="white")

FONT = ("Human",9,"bold")

# Label
label = tkinter.Label(text="is equal to ",background="white",font=FONT)
label.grid(row=1, column=0)

label_m = tkinter.Label(text="Miles",background="white",font=FONT)
label_m.grid(row=0, column=2)

label_k = tkinter.Label(text="Km",background="white",font=FONT)
label_k.grid(row=1, column=2)

label_result = tkinter.Label(text=0, background="white", font=FONT)
label_result.grid(row=1, column=1)
# Button

button = tkinter.Button(text="Calculate",font=FONT,command=button_click)
button.grid(row=2,column=1)

#Entry

input = tkinter.Entry(width=6)
input.grid(row=0,column=1,padx=10)

window.mainloop()
from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Digital Clock")
window.geometry("1000x400")
window.configure(bg="green")
window.resizable(False, False) 

clock_label = Label(
    window, bg="black", fg="white", font=("Arial", 135, "bold"), relief="flat"
)
clock_label.place(x=100, y=100)


def update_label():
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")

update_label()
window.mainloop()

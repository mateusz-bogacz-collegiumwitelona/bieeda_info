import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nowe Okno")
    label = tk.Label(new_window, text="To jest nowe okno!")
    label.pack()


root = tk.Tk()
root.title("Przycisk Otwierający Nowe Okno")

button = tk.Button(root, text="Otwórz Nowe Okno", command=open_new_window)
button.pack()

root.mainloop()

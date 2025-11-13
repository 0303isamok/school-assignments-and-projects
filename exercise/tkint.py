import tkinter as tk

root = tk.Tk()
root.title("Goat")
root.geometry("500x500")
root.configure(bg="lightgray")

label = tk.Label(root, text="I Like Fridge", font=("Arial", 18), bg="lightgray")
label.pack()

try:
    icon_image = tk.PhotoImage(file="https://raw.githubusercontent.com/0303isamok/school-assignments-and-projects/main/exercise/duckling_1.png")
    root.iconphoto(False, icon_image)
except tk.TclError as e:
    print("Error loading icon:", e)

root.mainloop()

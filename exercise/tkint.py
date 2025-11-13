import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Goat")

# Set the window size (width x height)
root.geometry("500x500")

# Set the background color
root.configure(bg="lightgray")

label = tk.Label(root, text="I Like Fridge", font=("Arial", 18))
label.pack()

icon_image = tk.PhotoImage(file="duckling_1.png")

# Start the Tkinter event loop
root.mainloop()
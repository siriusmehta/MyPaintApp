from tkinter import *


W=600
H=400


# create window
root = Tk()
root.title("My Paint App")
root.geometry("800x800")

# create a Canvas widget
my_canvas = Canvas(root, width=W, height=H, bg="white")
my_canvas.pack(pady=20)







root.mainloop()

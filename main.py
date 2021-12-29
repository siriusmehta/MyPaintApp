from tkinter import *
import tkinter.ttk as ttk

# Canvas Width and Height
W=600
H=400

def paint(e):

    # Brush Parameters
    brush_width = 20
    brush_color = "green"
    brush_type = ROUND

    x1 = e.x - 1
    y1 = e.y - 1

    x2 = e.x + 1
    y2 = e.y + 1

    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, smooth=True, width=brush_width, capstyle=brush_type)

def change_brush_size(event):
    """
    Change the size of the brush with default size of 10
    :return:
    """

    slider_label.config(text=int(my_slider.get()))


# create window
root = Tk()
root.title("My Paint App")
root.geometry("800x800")

# create a Canvas widget
my_canvas = Canvas(root, width=W, height=H, bg="white")

# put the Canvas on the main window
my_canvas.pack(pady=20)

#bind the mouse event of Left click button press mouse motion with Canvas
my_canvas.bind('<B1-Motion>', paint)

# Create Brush options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Adding Brush Size Frame
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Slider")
brush_size_frame.grid(row=0 ,column=0, padx=50)

my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush slider label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)













root.mainloop()

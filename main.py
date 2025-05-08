import turtle

# Constants for font size and spacing
font_size = 20
font_height = font_size
font_width = font_size * (1 - 0.39)

# Provided function – do not modify
def draw_letter(turtle, letter):
    height = font_size
    turtle.setx(turtle.xcor() - (font_width / 2))
    turtle.sety(turtle.ycor() - (height / 2))
    turtle.write(letter, font=('Courier', font_size))
    turtle.setx(turtle.xcor() + (font_width / 2))
    turtle.sety(turtle.ycor() + (height / 2))

# Exercise 1
def draw_carbon(t):
    """Draws a single CH₂ group (Carbon with 2 Hydrogens)"""
    # Draw H to the top
    t.setheading(90)  # Point up
    t.penup()
    t.forward(font_height)
    draw_letter(t, 'H')
    t.backward(font_height)

    # Draw H to the bottom
    t.setheading(270)  # Point down
    t.forward(font_height)
    draw_letter(t, 'H')
    t.backward(font_height)

    # Draw C at the center
    draw_letter(t, 'C')

    # Move forward to prepare for next bond
    t.setheading(0)
    t.pendown()
    t.forward(font_width)
    t.penup()


# Exercise 2
def draw_carbons(t, num_carbons):
    """Draws a straight line of CH₂ groups (without extra Hs at ends)"""
    for _ in range(num_carbons):
        draw_carbon(t)


# Exercise 3
def draw_carbon_chain(t, num_carbons):
    """Draws full CH₃–(CH₂)_n–CH₃ style carbon chain"""    
    t.speed(0)
    t.penup()

    # Start by drawing left end carbon with 3 Hs
    t.setheading(90)
    t.forward(font_height)
    draw_letter(t, 'H')
    t.backward(font_height * 2)
    draw_letter(t, 'H')
    t.forward(font_height)

    draw_letter(t, 'C')
    t.setheading(0)
    t.pendown()
    t.forward(font_width)
    t.penup()

    # Draw middle CH₂ units
    for _ in range(num_carbons):
        draw_carbon(t)

    # Draw last carbon with 3 Hs
    draw_letter(t, 'C')

    t.setheading(90)
    t.forward(font_height)
    draw_letter(t, 'H')
    t.backward(font_height * 2)
    draw_letter(t, 'H')

    # Hide turtle and finish
    t.hideturtle()



"""
*** USER INTERFACE CODE - DO NOT MODIFY ***

Below is the code to a Graphical User Interface.  You can use the buttons to 
interact with each of the draw functions to check if you have
implemented them correctly.
"""

import tkinter as tk
from tkinter import simpledialog

# GUI with Tkinter
def main_gui():
    root = tk.Tk()
    root.title("Carbon Chain Drawer")

    canvas = turtle.ScrolledCanvas(master=root)
    canvas.pack()
    global t    
    t = turtle.RawTurtle(canvas)
    t.hideturtle()

    def clear_drawing():
        t.clear()
        t.penup()
        t.goto(0, 0)

    def call_draw_carbon():
        clear_drawing()
        draw_carbon(t)

    def call_draw_carbons():
        clear_drawing()
        n = simpledialog.askinteger("Input", "How many CH₂ units?", minvalue=1)
        if n:
            draw_carbons(t, n)

    def call_draw_chain():
        clear_drawing()
        n = simpledialog.askinteger("Input", "How many CH₂ units in chain (excluding ends)?", minvalue=0)
        if n is not None:
            draw_carbon_chain(t, n)

    frame = tk.Frame(root)
    frame.pack()

    tk.Button(frame, text="Draw CH₂", command=call_draw_carbon).pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Draw (CH₂)n", command=call_draw_carbons).pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Draw Full Chain", command=call_draw_chain).pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Clear", command=clear_drawing).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
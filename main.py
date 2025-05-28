# Constants for font size and spacing
font_size = 20
font_height = font_size
font_width = font_size * (1 - 0.39)

# Provided function – do not modify
def draw_letter(t, letter):
    height = font_size
    t.setx(t.xcor() - (font_width * 0.6))
    t.sety(t.ycor() - (font_height * 0.8))
    t.write(letter, font=('Courier', font_size))
    t.setx(t.xcor() + (font_width * 0.6))
    t.sety(t.ycor() + (font_height * 0.8))

# Exercise 1
def draw_carbon(t):
    """Draws a single CH₂ group (Carbon with 2 Hydrogens)"""

    # Draw C at the center
    draw_letter(t, 'C')

    # Draw H to the top
    t.left(90)  # Point up
    t.penup()
    t.forward(font_height)
    t.pendown()
    t.forward(font_height)
    t.penup()
    t.forward(font_height)
    draw_letter(t, 'H')
    t.backward(font_height*4)
    t.pendown()
    t.backward(font_height)
    t.penup()
    t.backward(font_height)
    t.penup()

    # Draw H to the bottom
    draw_letter(t, 'H')
    t.forward(font_height * 3)
    t.right(90)
    t.pendown()



# Exercise 2
def draw_carbons(t, num_carbons):
    """Draws a straight line of CH₂ groups (without extra Hs at ends)"""
    for _ in range(num_carbons):
        draw_carbon(t)
        t.penup()
        t.forward(font_width)
        t.pendown()
        t.forward(font_width)
        t.penup()
        t.forward(font_width)


# Exercise 3
def draw_carbon_chain(t, num_carbons):
    """Draws full CH₃–(CH₂)_n–CH₃ style carbon chain"""    
    
    draw_letter(t, 'C')
    t.penup()
    t.forward(font_width)
    t.pendown()
    t.forward(font_width)
    t.penup()
    t.forward(font_width)

    draw_carbons(t, num_carbons)

    # Draw last carbon with 3 Hs
    draw_letter(t, 'C')




"""
*** USER INTERFACE CODE - DO NOT MODIFY ***

Below is the code to a Graphical User Interface.  You can use the buttons to 
interact with each of the draw functions to check if you have
implemented them correctly.
"""

# GUI with Tkinter
def main_gui():
    import tkinter as tk
    from tkinter import simpledialog

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
    import turtle
    main_gui()
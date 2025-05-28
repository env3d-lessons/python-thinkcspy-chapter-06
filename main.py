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

    # Below we are simply calling draw_letter to draw the letters C and H
    # You will need to modify this function to draw the CH₂ group correctly.
    draw_letter(t, 'C')
    draw_letter(t, 'H')
    draw_letter(t, 'H')



# Exercise 2
def draw_carbons(t, num_carbons):
    """Draws a straight line of CH₂ groups (without extra Hs at ends)"""
    # pass simply does nothing, you will need to replace it with your code.
    pass


# Exercise 3
def draw_carbon_chain(t, num_carbons):
    """Draws full CH₃–(CH₂)_n–CH₃ style carbon chain"""    
    # pass simply does nothing, you will need to replace it with your code.
    pass
    


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
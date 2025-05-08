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
def draw_carbon_chain(num_carbons):
    """Draws full CH₃–(CH₂)_n–CH₃ style carbon chain"""
    t = turtle.Turtle()
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



wn = turtle.Screen()
steve = turtle.Turtle()
draw_carbon(steve)
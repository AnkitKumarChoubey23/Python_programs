import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Circle Drawer")

# Ask the user for the background color, radius, and color of the circle
background_color = input("Enter the background color: ")
radius = int(input("Enter the radius of the circle: "))
circle_color = input("Enter the color of the circle: ")

# Set the background color
screen.bgcolor(background_color)

# Create a turtle object
circle_turtle = turtle.Turtle()

# Set the circle color
circle_turtle.fillcolor(circle_color)
circle_turtle.begin_fill()

# Draw the circle
circle_turtle.circle(radius)
circle_turtle.end_fill()

# Ask the user if they want another circle
while True:
    another = input("Do you want to draw another circle? (yes/no): ").strip().lower()
    if another == "yes":
        radius = int(input("Enter the radius of the next circle: "))
        circle_color = input("Enter the color of the next circle: ")
        circle_turtle.fillcolor(circle_color)
        circle_turtle.begin_fill()
        circle_turtle.circle(radius)
        circle_turtle.end_fill()
    elif another == "no":
        print("All circles drawn. Enjoy!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")

# Keep the window open until clicked
turtle.done()
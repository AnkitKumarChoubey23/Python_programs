import turtle
import time

# Ask for dimensions of the rectangle
rect_width = int(input("Enter the width of the rectangle: "))
rect_height = int(input("Enter the height of the rectangle: "))

# Create the screen
screen = turtle.Screen()
screen.title("Traffic Signal")

# Create the traffic signal frame
signal = turtle.Turtle()
signal.penup()
signal.goto(-rect_width // 2, rect_height // 2)
signal.pendown()
signal.fillcolor("black")
signal.begin_fill()
for _ in range(2):
    signal.forward(rect_width)
    signal.right(90)
    signal.forward(rect_height)
    signal.right(90)
signal.end_fill()

# Create the three lights
light_radius = min(rect_width, rect_height // 4) // 2  # Slightly smaller circles
positions = [
    (0, rect_height // 2 - light_radius * 2),  # Top position (Red light)
    (0, 0),                                  # Middle position (Yellow light)
    (0, -rect_height // 2 + light_radius * 2) # Bottom position (Green light)
]

lights = []
colors = ["red", "yellow", "green"]

for pos, color in zip(positions, colors):
    light = turtle.Turtle()
    light.penup()
    light.goto(pos)
    light.pendown()
    light.fillcolor("gray")  # Default off state
    light.shape("circle")
    light.shapesize(light_radius / 10)
    lights.append(light)

# Function to turn on a specific light
def turn_on_light(index):
    for i, light in enumerate(lights):
        light.fillcolor(colors[i] if i == index else "gray")

# Simulate the traffic signal
while True:
    for i in range(3):  # Alternate between Red, Yellow, Green
        turn_on_light(i)
        time.sleep(5)  # Light stays on for 5 seconds70
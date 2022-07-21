# COMP1021 Lab 2 Python Sketchbook
# Name:
# Student ID:
# Email: 

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

##### Initialize the colour
fillcolor = "black"
turtle.pencolor("black")
turtle.fillcolor(fillcolor)

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        #Ask
        turn_angle = int(input("Please enter the angle of rotation: "))

        if turn_angle>0:
            turtle.left(turn_angle)

        else:
            turn_angle = -turn_angle
            turtle.left(turn_angle)

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        #Ask
        width = int(input("Please enter the width of the rectangle: "))
        height = int(input("Please enter the height of the rectangle: "))

        turtle.begin_fill()
        
        for i in range(2):

            turtle.forward(width)

            turtle.left(90)

            turtle.forward(height)

            turtle.left(90)
            
        turtle.end_fill()
        

    ##### Handle the circle option
    if option == "c":
        print()

        #Ask
        radius = int(input("Please enter the radius of the circle: "))

        turtle.begin_fill()
        
        turtle.circle(radius)
        
        turtle.end_fill()
        

    ##### Handle the pen colour option
    if option == "p":
        print()

        #Ask
        pencolor = input("Please enter a colour name for the pen colour: ")
        turtle.pencolor(pencolor)

        
    ##### Handle the fill colour option
    if option == "f":
        print()

        #Ask
        fillcolor = input("Please enter a colour name for the fill colour: ")
        turtle.fillcolor(fillcolor)


    ##### Handle the fill colour option
    if option == "g":
        print()

        #Ask
        petal_size = int(input("Please enter the size of the flower petal: "))

        for petals in range(12):

            for triangles in range(3):
                turtle.forward(petal_size)
                turtle.left(120)

            turtle.left(30)


    ##### Handle the fill colour option
    if option == "e":
        print()

        #Ask
        explosion_size = int(input("Please enter the size of the explosion (>150): "))

        org_pencolor = turtle.pencolor()
        org_fillcolor = turtle.fillcolor()

        for colour in ["DarkOrchid", "firebrick", "DarkOrange", "gold"]:
            for j in range(1,5):
                turtle.color(colour + str(j))
                turtle.dot(explosion_size)
                explosion_size = explosion_size - 10

        turtle.pencolor(org_pencolor)
        turtle.fillcolor(org_fillcolor)

    ##### Handle the fill colour option
    if option == "a":
        print()

        #Do
        turtle.reset()
        turtle.width(4)
        turtle.speed(10)

        #Making "S"
        turtle.color("firebrick4")
        turtle.circle(25, -180)
        turtle.up()
        turtle.goto(0,-50)
        turtle.down()
        turtle.right(180)
        turtle.circle(25, 180)

        #Making "M"
        turtle.color("gold4")
        turtle.up()
        turtle.goto(50,-50)
        turtle.down()
        turtle.goto(50,50)
        turtle.goto(75, -50)
        turtle.goto(100, 50)
        turtle.goto(100, -50)

        turtle.up()
        turtle.goto(150, 0)
        turtle.right(180)
        turtle.down()

        #Making "S"
        turtle.color("firebrick4")
        turtle.circle(25, -180)
        turtle.up()
        turtle.goto(150, -50)
        turtle.down()
        turtle.right(180)
        turtle.circle(25, 180)

        turtle.up()
        turtle.goto(175, 50)
        turtle.right(180)
        turtle.down()

        #Making "T"
        turtle.color("DarkOrchid4")
        turtle.forward(75)
        turtle.backward(37.5)
        turtle.right(90)
        turtle.forward(100)  


turtle.done()


# Name: Seyyid Muhammadh Shafak Thaika

# Student ID: 20816388

# Email: smst@connect.ust.hk


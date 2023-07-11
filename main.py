# Maze Game Making
import math
import turtle
import random

# BY KRISHNENDU TALUKDAR

sc = turtle.Screen()
sc.bgcolor("black")
sc.title("A MAZE GAME")
sc.setup(700, 700)

# Registering shape
turtle.addshape("soldier_up.gif")
turtle.addshape("soldier_right.gif")
turtle.addshape("soldier_down.gif")
turtle.addshape("soldier_left.gif")
turtle.addshape("wall1.gif")
turtle.addshape("treasure1.gif")
turtle.addshape("dragon.gif")


# Let's Create A Pen
ben = turtle.Turtle()
ben.shape("square")
ben.color("white")
ben.penup()
ben.speed(0)

# Create a player for moving th maze properly

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("soldier_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
    # Let's Create direction
    def go_up(self):
        # Calculating the spot to move
        mv_to_x = plyr.xcor()
        mv_to_y = plyr.ycor() + 24

        self.shape("soldier_up.gif")
        # Check if the space got walls
        if (mv_to_x, mv_to_y) not in walls:
            self.goto(mv_to_x, mv_to_y)
    def go_down(self):
        # Calculating the spot to move
        mv_to_x = plyr.xcor()
        mv_to_y = plyr.ycor() - 24
        # Check if the space got walls

        self.shape("soldier_down.gif")


        if (mv_to_x, mv_to_y) not in walls:
            self.goto(mv_to_x, mv_to_y)
    def go_left(self):
        # Calculating the spot to move
        mv_to_x = plyr.xcor() - 24
        mv_to_y = plyr.ycor()

        self.shape("soldier_left.gif")

        # Check if the space got walls
        if (mv_to_x, mv_to_y) not in walls:
            self.goto(mv_to_x, mv_to_y)

    def go_right(self):
        # Calculating the spot to move
        mv_to_x = plyr.xcor() + 24
        mv_to_y = plyr.ycor()

        self.shape("soldier_right.gif")

        # Check if the space got walls
        if (mv_to_x, mv_to_y) not in walls:
            self.goto(mv_to_x, mv_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        dist = math.sqrt((a ** 2 ) + (b ** 2))

        if dist < 5:
            return True
        else:
            return False

# Lets make the treasure for the player
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure1.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



# Lets make a enemy dragon
class Dragon(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("dragon.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction ==  "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # Checking if the player is closer or not and if he is kill him dragons
        if self.is_close(plyr):
            if plyr.xcor() < self.xcor():
                self.direction = "left"
            elif plyr.xcor() > self.xcor():
                self.direction = "right"
            elif plyr.ycor() < self.ycor():
                self.direction = "up"
            elif plyr.ycor() > self.ycor():
                self.direction = "down"


        # Calculating the spot to move
        mv_to_x = self.xcor() + dx
        mv_to_y = self.ycor() + dy

        # Check if there wall
        if(mv_to_x, mv_to_y) not in walls:
            self.goto(mv_to_x, mv_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        # Setting timer to move on time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        u = self.xcor()-other.xcor()
        v = self.ycor()-other.ycor()
        distance = math.sqrt((u ** 2) + (v ** 2))

        if distance < 75:
            return True
        else:
            return False


    def destory(self):
        self.goto(2000, 2000)
        self.hideturtle()

# The Maze Levels
lev_maze = [""]

#The Maze
lev_1=[
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XPXXXXXXXXXX            X",
    "X  XXXXXXXXX  XXXXXXXXXXX",
    "X  XXXXXXXXX  XXXXXXXXXXX",
    "X       XXXX  XXXXXXXXXXX",
    "XXXXXX  XXXX  XXXXXXXXXXX",
    "XXXXXX  XXXX  XXXXXXXXXXX",
    "X XXXX  XXXX          XXX",
    "X XXXX  XXXXXXXXXXXX  XXX",
    "X       XXXXXXXXXXXX  XXX",
    "XXXXXX  XXXXXXXXXX    XXX",
    "XXXXXX  X     XXXX  XXXXX",
    "XXXXXX  X  XXXXXXX  XXXXX",
    "XXXXXX  X  XXXXXXX  XXXXX",
    "XXXXXX  X  XD          TX",
    "XXXT X  X  XXXXXXX  XXXXX",
    "XXX  X  X  XXXXXXX  XXXXX",
    "XXX     X  XXXXX    XXXXX",
    "XXXXXX  X  XXXXX  XXXXXXX",
    "XXXXXX  X  XXX    XXXXXXX",
    "XXXXXX  X  XXX  XXXXXXXXX",
    "XXXXXX  X  XXX  XXXXXXXXX",
    "X      DX  XXX       DXXX",
    "XXXXXX  XX  XX  XXXX  XXX",
    "XXXXXX          XXXX   TX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"]


# Treasure list
treasures = []

# Dragon lit
dragons = []

# Adding the maze to mazes list
lev_maze.append(lev_1)



# Creating A Level setup Function
def set_maze(lev_maze):
    for y in range(len(lev_maze)):
        for x in range(len(lev_maze[y])):
            # Getting the character at each x and y co-ordinate
            # Note the order of y and x in the next line
            chrctr = lev_maze[y][x]
            # Calculating the screen x and y co-ordinates
            scrn_x = -288 + (x * 24)
            scrn_y = 288 - (y * 24)
            # Checking if it is an X or the walls
            if chrctr == "X":
                ben.goto(scrn_x, scrn_y)
                ben.shape("wall1.gif")
                ben.stamp()
                # Adding co-ordinates to wall list
                walls.append((scrn_x, scrn_y))

            if chrctr == "P":
                plyr.goto(scrn_x,scrn_y)

            # Checking if it is a T/Treasure
            if chrctr == "T":
                treasures.append(Treasure(scrn_x, scrn_y))

            if chrctr == "D":
                dragons.append(Dragon(scrn_x, scrn_y))

# Creating a Class Instances
#pen = Ben()
plyr = Player()


# Let's create a wall co-ordinate lists
walls = []

# Setup the maze level
set_maze(lev_maze[1])

# Keyboard Binding
turtle.listen()
turtle.onkey(plyr.go_left, "Left")
turtle.onkey(plyr.go_right, "Right")
turtle.onkey(plyr.go_up, "Up")
turtle.onkey(plyr.go_down, "Down")


# Lets move the Drogons
for dragon in dragons:
    turtle.ontimer(dragon.move, t=250)

# Turning off screen updates
sc.tracer(0)

# Main Game Loop
while True:
    # Checking player and treasure collision
    for treasure in treasures:
        if plyr.is_collision(treasure):
            # Add the treasure gold to the player gold
            plyr.gold += treasure.gold
            print("Player Gold: {}".format(plyr.gold))
            # Destroy the Treasure
            treasure.destroy()
            # Remove the treasure from reasures list
            treasures.remove(treasure)

    for dragon in dragons:
        if plyr.is_collision(dragon):
            print("AWWW YOU DIED!")
            break


    # Update the screeen
    sc.update()



######################################################
# Project: redacted
# UIN: redacted
# link: redacted
# redacted
#imports
import turtle
import random

#screen stufff
s = turtle.Screen()
s.setup(450, 450)
s.tracer(0)

#screen dimensions
width, height = s.screensize()
#game object lis5t
game_objects = [{"t": turtle.Turtle(), "x": 0, "y": -(height/2),
                         "radius": 10, "image": "frog.gif", "type": "play-screen-user"},{"t": turtle.Turtle(), "x": random.randint(-(width/2), (width/2)), "y": random.randint(-(height/2), (height/2)),
                         "radius": 10, "image": "pad.gif", "type": "play-screen-pad"}]

#game start variablwe
game_state = "start"

lanes = [-200, -150, -100, -50, 0, 50, 100, 150, 200]

level = 0

global_turtle = turtle.Turtle()

lives = 3

global_velocity = 1

color = ["red", "blue", "green", "white", "black"]

def set_game_state(string):
    global game_state
    game_state = string

def start_screen():
    # start screen stuff
    global global_turtle
    global color
    while (game_state == "start"):
        s.bgcolor(color[4])
        global_turtle.hideturtle()
        global_turtle.color(color[3])
        global_turtle.fillcolor(color[3])
        global_turtle.up()
        global_turtle.goto(-100, 0)
        global_turtle.down()
        global_turtle.write("GET TO THE OTHER SIDE GAME")
        global_turtle.up()
        global_turtle.goto(-100, -100)
        global_turtle.down()
        global_turtle.write("PRESS ENTER TO BEGIN")
        global_turtle.up()
        global_turtle.goto(-100, -200)
        global_turtle.down()
        global_turtle.write("USE ARROW KEYS TO MOVE")
        global_turtle.up()
        s.listen()
        s.onkeypress(lambda: set_game_state("play"), "Return")
        if(game_state == "play"):
            global_turtle.clear()
            s.bgcolor(color[2])


def end_screen():
    # end screen stuff
    global global_turtle
    global game_objects
    while (game_state == "end"):
        s.bgcolor(color[4])
        global_turtle.hideturtle()
        global_turtle.color(color[3])
        global_turtle.fillcolor(color[3])
        global_turtle.up()
        global_turtle.goto(-100, 0)
        global_turtle.down()
        global_turtle.write("GAME OVER")
        global_turtle.up()


def play_screen():
    global global_turtle, lives, level, global_velocity
    #for each lane make an enemy
    for i in lanes:
        game_objects.append({"t": turtle.Turtle(), "x": -(width/2), "y": i,
                             "radius": 10, "image": "anti-fbi-pc-version.gif", "type": "play-screen-hostile"})
    #play screen loop
    while (game_state == "play"):
        #scoreboard 
        global_turtle.hideturtle()
        global_turtle.penup()
        global_turtle.goto(width/2 - 100, height/2 - 25)
        global_turtle.pendown()
        global_turtle.write("LIVES: " + str(lives))
        global_turtle.penup()
        global_turtle.goto(width/2 - 100, height/2 - 50)
        global_turtle.write("LEVEL: " + str(level))

        
        for obj in game_objects:

            obj["t"].clear()
            s.addshape(obj["image"])
            obj["t"].shape(obj["image"])
            obj["t"].color(color[2])
            obj["t"].fillcolor(color[2])

            if (obj["type"] == "play-screen-hostile"):

                # setting the velocity of the enemies
                obj["x"] += global_velocity

                # keeps enemies from leaving the screen
                if obj["x"] >= (width/2):
                    obj["t"].up()
                    obj["x"] = -(width/2)
                    obj["t"].down()

                # checking if its in bounds
                if (((((obj["x"] - game_objects[0]["x"])**2) + ((obj["y"]-game_objects[0]["y"])**2))**0.5) < 20) and (lives != 0):
                    lives -= 1
                    game_objects[0]['x'] = 0
                    game_objects[0]['y'] = 20
            #level portal logic
            if (obj["type"] == "play-screen-pad"):
                    #@checks bounds
                if ((((obj["x"] - game_objects[0]["x"])**2) + ((obj["y"]-game_objects[0]["y"])**2))**0.5) < 20:
                    level += 1
                    global_velocity *= 3
                    obj["x"] = random.randint(-(width/2), (width/2))
                    obj["y"] = random.randint(-(height/2), (height/2))
                    #changes color on level up
                    s.bgcolor(color[random.randint(0,len(color) - 1)])\
                    #refreshing
                    obj["t"].clear()
            #checks if lives 
            if lives == 0:
                s.clearscreen()
                set_game_state("end")
            #input handling
            def up_frog():
                game_objects[0]["y"] += 25

            def right_frog():
                game_objects[0]["x"] += 25

            def left_frog():
                game_objects[0]["x"] -= 25

            def down_frog():  
                game_objects[0]["y"] -= 25

            s.listen()
            s.onkey(up_frog, "Up")
            s.onkey(right_frog, "Right")
            s.onkey(left_frog, "Left")
            s.onkey(down_frog, "Down")

            obj["t"].goto(obj["x"], obj["y"])
            obj["t"].clear()

        global_turtle.clear()
        s.update()


def main():
    #initialize
    start_screen()
    play_screen()
    end_screen()


main()

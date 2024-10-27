import turtle as trtl
import keyboard
import random
# Set up the game
runner = trtl.Turtle()
rock = trtl.Turtle()
runner.speed(3)
runner.penup()
rock.penup()
#set positions
runner.left(90)
runner.goto(-100,0)
rock.goto(100,0)
# set image of runner and rock
runner.register_shape("runner.png")
rock.register_shape("rock.png")
runner.shape("runner.png")
rock.shape("rock.png")



#FUNCTIONS
# Jump function
def jump():
 runner.forward(25)
 runner.backward(25)

wn = trtl.Screen()
wn.mainloop()

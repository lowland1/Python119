import turtle as trtl
import random
# Set up the game
score = 0
score_board = []
wn = trtl.Screen()
wn.register_shape("runner.gif")
wn.register_shape("rock.gif")
runner = trtl.Turtle()
rock = trtl.Turtle()
score_trtl = trtl.Turtle()
score_trtl.hideturtle()
runner.speed(0)
score_trtl.pensize(10)
rock.penup()
runner.penup()
score_trtl.penup()
#set positions
runner.goto(-400,50)
rock.left(180)
rock.goto(450,0)
score_trtl.goto(0,350)
score_trtl.pendown()
# set image of runner and rock
runner.shape("runner.gif")
rock.shape("rock.gif")

#FUNCTIONS
# Game over function
def game_over():
 global score
 global score_board
 score_trtl.write("GAME OVER, CURRENT SCORE IS:" + score + ", HIGH SCORE IS:" )
 score_board.append(score)


# Jump function
def jump(x,y):
 runner.sety(250)
 wn.ontimer(runner.sety(50),200)

# moving rock function
def move():
 rock.goto(rock.xcor()-50,0)
 if rock.distance(runner) < 10:
  game_over()
 if rock.xcor()< -500:
  rock.setx(450)
 wn.ontimer(move, 50)


#score function
def add_score():
 global score
 score += 1000
 score_trtl.clear()
 score_trtl.write(score, font='Arial', align='center')
 wn.ontimer(add_score,1000)


#CODE
wn.onclick(jump)
wn.ontimer(add_score,1000)
move()

 
wn.mainloop()

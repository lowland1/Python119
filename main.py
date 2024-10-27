import turtle as trtl

runner = trtl.Turtle()
rock = trtl.Turtle()
runner.register_shape("runner.png")
rock.register_shape("rock.png")
runner.shape("runner.png")
rock.shape("rock.png")
 
wn = trtl.Screen()
wn.mainloop()

# This is a function you can use in your game. Leave this code at the top,
# and use it as described below
import random
def shoot():
  hand = ["Rock", "Paper", "Scissors"]
  return random.choice( hand )
  
# example useage:
# run "shoot()" 3 times and store the result each time
# run this whole script several times to see how random it is
throw1 = shoot()
throw2 = shoot()
throw3 = shoot()
print ( throw1 )
print ( throw2 )
print ( throw3 )

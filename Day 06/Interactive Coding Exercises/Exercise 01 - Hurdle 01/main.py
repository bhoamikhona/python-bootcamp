####################################################################################################################################################################
# NOTE: This is a code for Reeborg's World                                                                                                                         #
# To see this code in action, go to Reeborg's World Hurdle 1, paste this code there and run.                                                                       #
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json    #
####################################################################################################################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for hurdle in range(6):
    jump()


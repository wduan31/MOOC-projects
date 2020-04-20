# http://www.codeskulptor.org/#user30_BNvjCbmhPU_4.py

import simplegui
import random
import math

list = []
num_cards = 16
frame_size = [50 * num_cards,100]
game_state = 0
#matches store the positions of the previously opened cards
match1 = 0
match2 = 0
turns = 0

list = []
list1 = []
for i in range(num_cards/2):
        list.append([i,0])
        list1.append([i,0])
list.extend(list1)

# helper function to initialize globals
def new_game():
    global game_state, list, match1, match2, turns
    for i in range(num_cards):
        list[i][1] = 0
    random.shuffle(list)
    game_state = 0
    match1 = 0
    match2 = 0
    turns = 0
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here 
    global list, game_state, match1, match2, turns
    t = math.floor((pos[0]+1)/50.0)
    if (t < num_cards):
        if (list[t][1] == 0):
            if game_state == 0:
                turns = turns + 1 
                # If there is no card opened previously, change the state of game, and change match to the currently opened card.
                match1 = t
                list[match1][1] = 1
                game_state = 1
            elif game_state == 1:
                match2 = t
                if (list[match2][0] == list[match1][0]):
                    list[match2][1] = 2
                    list[match1][1] = 2
                    game_state = 0
                else:
                    list[match2][1] = 1
                    game_state = 2
            else:
                turns = turns + 1 
                list[match1][1] = 0
                list[match2][1] = 0
                game_state = 1
                match1 = t
                list[match1][1] = 1
                   
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(num_cards):
         label.set_text("Turns = " + str(turns))
         if (list[i][1] == 0):
            canvas.draw_polygon([[50 * i,0],[50 * (i+1),0],[50 * (i+1),frame_size[1]],[50 * i,frame_size[1]]],2,"Red","Green")
         else:
            t = 50 * i +10
            canvas.draw_text(str(list[i][0]),[t, 70], 60, "White")     
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frame_size[0],frame_size[1] )
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

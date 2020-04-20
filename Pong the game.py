#http://www.codeskulptor.org/#user30_WbmCYQD2sR_5.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT/2]
    ball_vel = [0,0]
    a = -1
    if (direction):
        a = 1
    ball_vel[0] = a * (random.randrange(120, 180)/60)
    ball_vel[1] = -(random.randrange(60, 180)/60)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 ]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 ]
    paddle1_vel = 0
    paddle2_vel = 0
    dice = random.randint(0,1)
    if (dice):
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # If the ball hits lower or upper wall, it is bounced backwards
    if ((ball_pos [1] + BALL_RADIUS) >= (HEIGHT - 1)):
        ball_vel [1] = - ball_vel [1]
    if ((ball_pos [1] - BALL_RADIUS) <= 0):
        ball_vel [1] = - ball_vel [1]
    # update ball
    ball_pos [0] = ball_pos [0] + ball_vel [0] 
    ball_pos [1] = ball_pos [1] + ball_vel [1] 
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel 
    paddle2_pos[1] += paddle2_vel
    if (paddle1_pos [1] <= HALF_PAD_HEIGHT) :
        paddle1_pos [1] = HALF_PAD_HEIGHT
    if (paddle1_pos [1] >= (HEIGHT - HALF_PAD_HEIGHT)) :
        paddle1_pos [1] = (HEIGHT - HALF_PAD_HEIGHT)
    if (paddle2_pos [1] <= HALF_PAD_HEIGHT) :
        paddle2_pos [1] = HALF_PAD_HEIGHT
    if (paddle2_pos [1] >= (HEIGHT - HALF_PAD_HEIGHT)) :
        paddle2_pos [1] = (HEIGHT - HALF_PAD_HEIGHT)
        
    # If the ball hits either gutter, the opponent scores, and ball is respawned towards the winner
    # If the ball hits either paddle, it is bounced back.
    if ((ball_pos [0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH -1)):
        if ((ball_pos [1] > (paddle2_pos [1] + HALF_PAD_HEIGHT)) or (ball_pos [1] < (paddle2_pos [1] - HALF_PAD_HEIGHT))):
            score1 += 1
            spawn_ball(LEFT)
        else:
            ball_vel [0] = - (ball_vel [0] + ball_vel [0]/10)
    if ((ball_pos [0] - BALL_RADIUS) <= PAD_WIDTH):
        if ((ball_pos [1] > (paddle1_pos [1] + HALF_PAD_HEIGHT)) or (ball_pos [1] < (paddle1_pos [1] - HALF_PAD_HEIGHT))):
            score2 += 1
            spawn_ball(RIGHT)
        else:
            ball_vel [0] = - (ball_vel [0] + ball_vel [0]/10)    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS, 2, "White")
    # draw paddles
    ul1 = [paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1] - HALF_PAD_HEIGHT]
    ur1 = [paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] - HALF_PAD_HEIGHT]
    dl1 = [paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT]
    dr1 = [paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT]
    ul2 = [paddle2_pos[0] - HALF_PAD_WIDTH , paddle2_pos[1] - HALF_PAD_HEIGHT]
    ur2 = [paddle2_pos[0] + HALF_PAD_WIDTH , paddle2_pos[1] - HALF_PAD_HEIGHT]
    dl2 = [paddle2_pos[0] - HALF_PAD_WIDTH , paddle2_pos[1] + HALF_PAD_HEIGHT]
    dr2 = [paddle2_pos[0] + HALF_PAD_WIDTH , paddle2_pos[1] + HALF_PAD_HEIGHT]
    canvas.draw_polygon([ul1,ur1,dr1,dl1],2,"White","White")
    canvas.draw_polygon([ul2,ur2,dr2,dl2],2,"White","White")
    # draw scores
    canvas.draw_text (str(score1),[WIDTH/4,HEIGHT/4],50,"White")
    canvas.draw_text (str(score2),[(3 *WIDTH / 4),HEIGHT/4],50,"White")
def keydown(key):
    vec = 120/60
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP ["w"] :
        paddle1_vel = -vec
    if key == simplegui.KEY_MAP ["s"] :
        paddle1_vel = vec
    if key == simplegui.KEY_MAP ["up"] :
        paddle2_vel = -vec
    if key == simplegui.KEY_MAP ["down"] :
        paddle2_vel = vec
    pass

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",new_game,100)

# start frame
new_game()
frame.start()

# http://www.codeskulptor.org/#user31_LyZpuLxGNy_7.py
import simplegui
# define global variables
t = 0
timer_on = 0
total_stop = 0
suc_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth = t % 10
    tsec = t // 10
    min = tsec // 60
    sec = tsec % 60
    if sec <10:
        sec = "0" + str(sec)
    else:
        sec = str(sec)
    t_str = str(min) + ":" + sec + "." + str(tenth)
    return t_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global timer_on
    timer.start()
    timer_on = 1
    pass

def Stop ():
    timer.stop()
    global timer_on
    global total_stop
    global suc_stop
    if timer_on :
        total_stop = total_stop + 1
        timer_on = 0
        if (t % 10) == 0:
            suc_stop = suc_stop + 1
    pass

def Reset ():
    global t 
    global timer_on 
    global total_stop 
    global suc_stop
    timer.stop()
    t = 0
    timer_on = 0
    total_stop = 0
    suc_stop = 0
    pass

# define event handler for timer with 0.1 sec interval
def count ():
    global t
    t = t + 1
    pass	

# define draw handler
def draw(canvas):
    canvas.draw_text (format(t),[130,150],40,"White")
    canvas.draw_text ((str(suc_stop) + "/" + str(total_stop)), [260,20], 20 , "Blue")
   
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 300)
timer = simplegui.create_timer(100, count)
# register event handlers
frame.set_draw_handler (draw)
frame.add_button ("Start",Start,100)
frame.add_button ("Stop",Stop,100)
frame.add_button ("Reset",Reset,100)

# start frame
frame.start()

# Please remember to review the grading rubric

# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
win = 0
amount =0
scores = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = (t - 600 * A) // 100
    C = (t - 600 * A - 100 * B) // 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
	
# if timer stop between 4.8 to 5.0 every five seconds, you get one
def grade(t):
    global scores
    global win
    global amount
    temp = t % 100
    if t != 0:
        if ((temp >= 48 and temp <= 50) or
             temp >= 98 or
             temp == 0):
            win += 1
        amount += 1
    scores = str(win)+'/'+str(amount)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def time_start():
    timer.start()
    
def time_stop():
    timer.stop()
    grade(time)
   
def time_reset():
    global time
    global win
    global sum
    global scores
    time = 0
    win = 0
    sum = 0
    scores = "0/0"
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def update():
    global time
    time += 1

# define draw handler
def	draw_handler(canvas):
    canvas.draw_text(scores, (230, 30), 30, 'Green')
    canvas.draw_text(format(time), (80, 110), 50, 'White')
        
# create frame
frame = simplegui.create_frame("Game", 300, 200)

# register event handlers
frame.set_draw_handler(draw_handler)
button1 = frame.add_button("Start", time_start, 100)
button2 = frame.add_button("Stop", time_stop, 100)
button3 = frame.add_button("Reset", time_reset, 100)
timer = simplegui.create_timer(100, update)

# start frame
frame.start()

# Please remember to review the grading rubric

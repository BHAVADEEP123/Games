import random
from tkinter import *
from constants import *

class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0]) 
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)
        canvas.itemconfig(self.squares[0],fill='#FFFF00')

class Food:
    def __init__(self):
        x = random.randint(0,GAME_WIDTH/SPACE_SIZE-1)*SPACE_SIZE
        y = random.randint(0,GAME_HEIGHT/SPACE_SIZE-1)*SPACE_SIZE

        self.coordinates = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")



def next_turn(snake,food):
    global score,speed
    
    x,y = snake.coordinates[0]
    if direction == 'up':
        y-=SPACE_SIZE
    elif direction=='down':
        y+=SPACE_SIZE
    elif direction=='left':
        x-=SPACE_SIZE
    elif direction=='right':
        x+=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    canvas.itemconfig(snake.squares[0],fill=SNAKE_COLOR)
    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill='#FFFF00')
    snake.squares.insert(0,square)
    

    if x==food.coordinates[0] and y==food.coordinates[1]:
        score+=1
        if(score==5):
            speed=170
        elif(score==20):
            speed=150
        elif(score==25):
            speed=100
        elif(score==30):
            speed=75
        
        lable.config(text ="score:{}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake)==1:
        game_over(1)
    elif check_collision(snake)==2:
        game_over(2)
    else:
        window.after(speed,next_turn,snake,food)  #window.after(delay_in_milliseconds, function_name, *args)

def change_direction(new_direction): 
    global direction
    if(direction=='left'):
        if(new_direction!='right'):
           direction = new_direction 
    if(direction=='right'):
        if(new_direction!='left'):
            direction = new_direction
    if(direction=='up'):
        if(new_direction!='down'):
            direction = new_direction
    if(direction=='down'):
        if(new_direction!='up'):
            direction = new_direction
            
def check_collision(snake):
    x,y = snake.coordinates[0]
    if(x<0 or x>=GAME_WIDTH or y<0 or y>=GAME_HEIGHT):
        return 1
    for x1,y1 in snake.coordinates[1:]:
        if x1==x and y1==y:
            return 2

def game_over(type):
    canvas.delete(ALL)
    if type==1 :
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER\n\n",fill="red")
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',30),text="wall collision",fill="red")
        
    elif type==2:
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER\n\n",fill="red")
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',30),text="body collision",fill="red")


window = Tk()
window.title("Snake Game")
window.resizable(False,False)

score = 0
direction = 'down'
lable = Label(window,text ="score:{}".format(score),font=('consolas',40))
lable.pack()

canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
x = screen_width//2-window_width//2
y = screen_height//2-window_height//2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))

snake = Snake()
food = Food()
speed = SPEED
next_turn(snake,food)

window.mainloop()
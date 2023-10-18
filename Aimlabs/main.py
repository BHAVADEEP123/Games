import random
from tkinter import *
from constants import *
import time
import threading

class Target:
    def __init__(self) -> None:
        self.lifeTime = 2000
        self.coordinates = []
        self.targets = []
        for i in range(0,NUMBER_OF_TARGETS):
            x = random.randint(1*window.winfo_screenwidth()//4//MAX_RADIUS-1,3*window.winfo_screenwidth()//4//MAX_RADIUS-1)*MAX_RADIUS
            y = random.randint(1*window.winfo_screenheight()//4//MAX_RADIUS-1,3*window.winfo_screenheight()//4//MAX_RADIUS-1)*MAX_RADIUS
            self.coordinates.append([x,y])
        for x,y in self.coordinates:
            target = canvas.create_oval(x,y,x+MAX_RADIUS,y+MAX_RADIUS,fill="yellow",tag="target")
            self.targets.append((target,time.time()))
            # print(str(time.time())+",")
            time.sleep(2/totalTargets)
        
def collapse():
    global allTargets,run,totalTargets
    while(run):
        for i in range(len(allTargets.targets)):
            if(time.time()-allTargets.targets[i][1]>=2):
                canvas.delete(allTargets.targets[i][0])
                del allTargets.targets[i]
                del allTargets.coordinates[i]
                x = random.randint(1*WINDOW_WIDTH//4//MAX_RADIUS-1,3*WINDOW_WIDTH//4//MAX_RADIUS-1)*MAX_RADIUS
                y = random.randint(1*WINDOW_HEIGHT//4//MAX_RADIUS-1,3*WINDOW_HEIGHT//4//MAX_RADIUS-1)*MAX_RADIUS
                allTargets.coordinates.append([x,y])
                tempTarget = canvas.create_oval(x,y,x+MAX_RADIUS,y+MAX_RADIUS,fill="yellow",tag="target")
                allTargets.targets.append((tempTarget,time.time()))
                # print(str(time.time())+",")
                totalTargets+=1
                lable.config(text="score:{} of {}".format(perfectHits,totalTargets))
                if(run==False):
                    return

def hit():
    global allTargets


window = Tk()
window.title("Aim labs")
window.resizable(False,False)

perfectHits = 0
totalTargets = NUMBER_OF_TARGETS

lable = Label(window,text="score:{} of {}".format(perfectHits,totalTargets),font=('consolas',40))
lable.pack()
canvas = Canvas(window,bg="blue",height=window.winfo_screenheight(),width=window.winfo_screenwidth())
canvas.pack()
window.update()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+{-8}+{-8}")

WINDOW_WIDTH = window.winfo_screenwidth()
WINDOW_HEIGHT = window.winfo_screenheight()

allTargets = Target()
start_thread = threading.Thread(target=collapse)
run = True
start_thread.start()

window.mainloop()
run = False
start_thread.join()
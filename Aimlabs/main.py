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
            self.targets.append([target,time.time()])
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
                    canvas.delete(ALL)
                    return
        

def hit(event):
    global allTargets,totalHits,perfectHits,run,totalTargets
    totalHits+=1
    for i in range(len(allTargets.targets)):
        object_coords = canvas.coords(allTargets.targets[i][0])
        center_x = (object_coords[0]+object_coords[2])/2
        center_y = (object_coords[1]+object_coords[3])/2
        radius = abs(object_coords[2]-center_x)
        if((event.x-center_x)**2+(event.y-center_y)**2)<=radius**2:
            # run = False
            # start_thread1.join()
            perfectHits+=1
            # allTargets.targets[i][1]+=2
            canvas.delete(allTargets.targets[i][0])
            
            x = random.randint(1*WINDOW_WIDTH//4//MAX_RADIUS-1,3*WINDOW_WIDTH//4//MAX_RADIUS-1)*MAX_RADIUS
            y = random.randint(1*WINDOW_HEIGHT//4//MAX_RADIUS-1,3*WINDOW_HEIGHT//4//MAX_RADIUS-1)*MAX_RADIUS
            allTargets.coordinates.append([x,y])
            tempTarget = canvas.create_oval(x,y,x+MAX_RADIUS,y+MAX_RADIUS,fill="yellow",tag="target")
            allTargets.targets[i]=[tempTarget,time.time()]
            totalTargets+=1
            lable.config(text="score:{} of {}".format(perfectHits,totalTargets))
            # run = True
            # start_thread1.join()

        

def stop_thread():
    global run
    run = False
    canvas.delete(ALL)
    accuracy = (perfectHits/(totalHits))*100
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',40),text="Perfect Hits: {}\n\n".format(perfectHits),fill="red")
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2+60,font=('consolas',40),text="Wrong Hits: {}\n\n".format(totalHits-perfectHits),fill="red")
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2+120,font=('consolas',40),text="Accuracy: {}\n\n".format(accuracy),fill="red")

window = Tk()
window.title("Aim labs")
window.resizable(False,False)

perfectHits = 0
totalHits = 0
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
start_thread1 = threading.Thread(target=collapse)
canvas.bind("<Button-1>",hit)
run = True
start_thread1.start()

window.after(TOTAL_TIME*1000,stop_thread)
    


window.mainloop()
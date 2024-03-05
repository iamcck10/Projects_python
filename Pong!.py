from tkinter import *
import random
import time

counter=0
counter1=0


root=Tk()
root.title=("Bounce!")
root.resizable(0,0)
root.wm_attributes("-topmost",1)

canvas = Canvas(root,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg='black')
canvas.pack()

root.update()

canvas.create_line(250,0,250,400,fill='white')

class Ball:
    def __init__(self,canvas,paddle,paddle1,color):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle1=paddle1
        self.id=canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id,235,200)
        starts=[-2,2]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-2
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self,pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle1_pos[1] and pos[1]<=paddle1_pos[3]:
            if pos[2]>=paddle1_pos[0] and pos[2]<=paddle1_pos[2]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=2
        if pos[3]>=self.canvas_height:
            self.y=-2
        if pos[0]<=0:
            self.x=2
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-2
            self.score(False)
        if self.hit_paddle(pos)==True:
            self.x=2
        if self.hit_paddle1(pos)==True:
            self.x=-2

    def score(score,val):
        global counter
        global counter1
        
        if val==True:
            a=canvas.create_text(125,40,text=counter,font=("Arial",60),fill='white')
            canvas.itemconfig(a,fill='black')
            counter+=1
            a=canvas.create_text(125,40,text=counter,font=("Arial",60),fill='white')

        if val==False:
            a=canvas.create_text(375,40,text=counter1,font=("Arial",60),fill='white')
            canvas.itemconfig(a,fill='black')
            counter1+=1
            a=canvas.create_text(375,40,text=counter1,font=("Arial",60),fill='white')
            
        
        

class Paddle:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0
            
    def turn_left(self,evt):
        self.y=-2
        
    def turn_right(self,evt):
        self.y=2



class Paddle1:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(470,150,500,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0
            
    def turn_left(self,evt):
        self.y=2
        
    def turn_right(self,evt):
        self.y=-3



paddle=Paddle(canvas,'cyan')
paddle1=Paddle1(canvas,'pink')
ball=Ball(canvas,paddle,paddle1,'orange')


while 1 :
    ball.draw()
    paddle.draw()
    paddle1.draw()
    
    if counter==10:
        canvas.create_text(250,200,text="Congrats Player 2! You win!",font=32,fill="red")
        canvas.create_text(250,215,text="Score: "+str(counter)+" - "+str(counter1),font=32,fill="red")
        ball.canvas.move(self.id,235,200)
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle1.y=0
    if counter1==10:
        canvas.create_text(250,200,text="Congrats Player 1! You win!",font=32,fill="red")
        canvas.create_text(250,215,text="Score: "+str(counter)+" - "+str(counter1),font=32,fill="red")
        ball.canvas.move(self.id,235,200)
        ball.x=0
        ball.y=0
        paddle.y=0
        paddle1.y=0

    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    if counter == 10 or counter1 == 10:
        time.sleep(100000)
        



        

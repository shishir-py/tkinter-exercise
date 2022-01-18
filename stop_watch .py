
from cgitb import text
import time
from tkinter import *
from unittest import result
root=Tk()
root.title("Stopwatch")
root.geometry("400x300")
root.config(background="lightgray")
initial="00:00:00"
hour=00
sec=00
min=00


def clock():
    hour =time.strftime("%I")
    minute =time.strftime("%M")
    second =time.strftime("%S")
    factor =time.strftime("%p")
    input.config(text=hour +":"+minute+":"+second  +factor)
    input.after(1000,clock)
    
    
def start():
    global time, hour, sec, min        
    sec += 1 
    if sec==60:
        sec=00
        min=sec+1
    if min==60:
        min=00
        hour=min+1
    input.config(text=f'{hour}:{min}:{sec}')
    time = input.after(1000, start)
def stop():
    input.after_cancel(time)
def reset():
    global hour,min,sec
    hour=00
    min=00
    sec=00
    input.config(text=f'{hour}:{min}:{sec}')


heading =Label(root, text="welcome to stopwatch",height=1, bg="lightgray",font=('Arial',20),padx=10,pady=10).pack()
input = Label(root,text=initial,font=('Helvetica',48))
input.pack()
bt2 = Button(root,text="start", height=5, width=7,bg="green", command=start).pack(side=LEFT)
bt2 = Button(root,text="Stop",height=5, width=7,bg="red", command=stop).pack(side=LEFT)
bt3 = Button(root,text="Reset",height=5, width=7, bg="yellow", command=reset).pack(side=LEFT)
bt4 = Button(root, text="Time",height=5, width=7, command=clock).pack(side=LEFT)



root.mainloop()
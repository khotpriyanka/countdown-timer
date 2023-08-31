import time
import tkinter as tk
from tkinter import Entry, Label, Button

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        root.update()
        time.sleep(1)
        t -= 1

    time_label.config(text='Times Up!')

def start_timer():
    try:
        t = int(time_entry.get())
        countdown(t)
    except ValueError:
        time_label.config(text='Invalid Input')


root = tk.Tk()
root.title('Countdown Timer')

time_label  = Label(root, text = '', font = ('Helvetica', 48))
time_label.pack()

time_entry = Entry(root, font = ('Helvetica', 24))
time_entry.pack()

start_button = Button(root, text = 'Start Timer', command=start_timer)
start_button.pack()

root.mainloop()
    

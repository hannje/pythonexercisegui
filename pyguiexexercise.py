from datetime import datetime
import time
from random import seed
from random import randint
import tkinter as tk
import requests
from PIL import Image, ImageTk
from random import seed
from random import random


choices = [
    '25 pushups',
    '60 second plank',
    '30 situps',
    'bullworker',
    'bullworker',
    '2 minute stretch',
    '15 squats',
    '2 minute inversion',
    '2 minute stretch',
    '15 squats',
    '2 minute inversion',
    'elastic bands',
    'elastic bands',
    '25 pushups',
    '25 pushups',
    '25 pushups',
    'KettleBell',
    'Deadlift',
    'Deadlift',
    'KettleBell',
    '60 second plank',
    '60 second plank',
    '60 second plank',
    '30 situps',
    '30 situps']

def test_func( data):
    print("button click" + data)

def getlogfile():
    return 'exercse/log'

def rolldice():
    chs = len(choices)
    results = randint(0, chs-1)
    label['text'] = choices[results]

#    print(results)
def logcompletion():
    # seed random number generator
    #    seed(1)
    # generate some integers


    dateTimeObj = datetime.now()


    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")

    if len(label['text']) == 0:
        print('no activity chosen')
        return
    f = open("guru99.txt", "a+")
    f.write(timestampStr + ": " + label['text'] + '\n')

    f.close()
    print("done")

HEIGHT = 700
WIDTH = 500
app = tk.Tk()

canvas = tk.Canvas(app,height = HEIGHT,width = WIDTH)
canvas.pack()

frame = tk.Frame(app, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.7, relheight=.06, anchor='n')

lower_frame = tk.Frame(app,  bd=5)
lower_frame.place(relx=0.5, rely=0.15, relwidth=.7, relheight=.3, anchor='n')

lowest_frame = tk.Frame(app, bg='#DCDCDC', bd=5, highlightbackground="black")
lowest_frame.place(relx=0.5, rely=0.45, relwidth=.7, relheight=.3, anchor='n')


#entry = tk.Entry(frame)X

#ntry.place(relwidth=0.6, relheight=1)


button = tk.Button(frame, text="RollDice",
                   command=lambda: rolldice())
button.place(relx=.01,relheight = 1,relwidth = 0.3)




label = tk.Label(lower_frame, font=60, bd=4, bg='#00FFFF',highlightbackground="black")
label.place(relheight=1, relwidth=1)

button1 = tk.Button(lower_frame, text="LogCompletion", bg='#E0FFFF',fg='red', borderwidth=1, command=lambda: logcompletion())

button1.place(relx=.4, rely=0.10, relheight=.2, relwidth=0.3)



app.mainloop()


import schedule
import time
from threading import Thread
import tkinter as tk
import os
import datetime

minutes_interval = 0.5

inpDir = r"C:\Users\dahom\Desktop\ps_screen\input"
outDir = r"C:\Users\dahom\Desktop\ps_screen\output"
count = len(os.listdir(outDir))

def updateLabel():
    global count, minutes_interval
    newcount = len(os.listdir(outDir))
    rate =round( (newcount-count) / minutes_interval , 2)
    count = newcount
    
    goalCount = len(os.listdir(inpDir))
    estTime = (round((goalCount / rate),2)) if rate != 0 else 0
    now = datetime.datetime.now()
    now_plus = now + datetime.timedelta(minutes = int(estTime))
    final_est_time =now_plus.strftime("%H:%M:%S")
    
    currentTarget = len(os.listdir(inpDir))
    print(f"rate:{rate} estTime{estTime}")
    
    
    var.set(f"{currentTarget}\n{rate} S/{minutes_interval}\n{final_est_time}")
    
    
    

root = tk.Tk()
root.config(bg='white')
root.title("Estimator")
root.geometry('%dx%d+%d+%d' % (160, 130, 1020, 0))
root.resizable(0,0)
root.overrideredirect(1)
root.wm_attributes("-topmost", 1)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")


var = tk.StringVar()
var.set(0)
    
#root.mainloop()
w = tk.Label(root, textvariable=var , bg='gray99', font=("Courier", 18))
w.pack()

schedule.every(minutes_interval).minutes.do(updateLabel)

while True:
    root.update_idletasks()
    root.update()
    schedule.run_pending()
    time.sleep(5)



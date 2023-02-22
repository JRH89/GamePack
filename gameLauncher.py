import tkinter as tk
import subprocess
from tkinter import ttk
import sys
import os

if getattr(sys, 'frozen', False):
    import pyi_splash

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("Game Launcher")
style = ttk.Style()
style.theme_use("xpnative") 
style.configure("TFrame", background="white", relief="sunken", bd=3)

window_width = 200
window_height = 210
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.configure(background='dark green')
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

game_pack_label = tk.Label(root, text="GAME PACK", font=("Fixedsys", 25), fg="dark blue", bg="gray")
game_pack_label.grid(row=0, column=0, columnspan=2, pady=10)

game_pack_label = tk.Label(root, text="Hooker Hill Studios", font=("Lucida", 10), fg="dark blue", bg="dark green")
game_pack_label.grid(row=3, column=0, columnspan=2, pady=5)

game_pack_label = tk.Label(root, text="2023", font=("Lucida", 8), fg="dark blue", bg="dark green")
game_pack_label.grid(row=4, column=0, columnspan=2, pady=0)

def load_game(game_name):
    script_path = game_name
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.Popen(["python", script_path], shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)

import threading

def run_game_1():
    import pet
    t = threading.Thread(target=pet.start_game)
    t.start()

def run_game_2():
    import snake
    t = threading.Thread(target=snake.start_game)
    t.start()
    
def run_game_3():
    import pong
    t = threading.Thread(target=pong.start_game)
    t.start()
   
def run_game_5():
    import flash
    t = threading.Thread(target=flash.start_game)
    t.start()
    
game_1_button = ttk.Button(root, text="Screen Pet", command=run_game_1)
game_1_button.grid(row=1, column=0, pady=10, padx=10)

game_2_button = ttk.Button(root, text="Caterpillar", command=run_game_2)
game_2_button.grid(row=1, column=1, pady=10, padx=10)

game_3_button = ttk.Button(root, text="Ping-Pong", command=run_game_3)
game_3_button.grid(row=2, column=0, pady=10, padx=10)

game_5_button = ttk.Button(root, text="Flash Memory", command=run_game_5)
game_5_button.grid(row=2, column=1, pady=10, padx=10)

if getattr(sys, 'frozen', False):
    pyi_splash.close()

root.mainloop()

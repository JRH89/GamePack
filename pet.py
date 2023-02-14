def start_game():
    import tkinter
    from tkinter import HIDDEN, NORMAL, Tk, Canvas
    from tkinter import messagebox as msgbox
    
    root = Tk()
    root.title("Virtual Pet")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = 420
    window_height = 500
    
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def on_closing():
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
 
    def toggle_eyes():
        current_color = c.itemcget(eye_left, 'fill')
        new_color = c.body_color if current_color == 'white' else 'white'
        current_state = c.itemcget(pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        c.itemconfigure(pupil_left, state=new_state)
        c.itemconfigure(pupil_right, state=new_state)
        c.itemconfigure(eye_left, fill=new_color)
        c.itemconfigure(eye_right, fill=new_color)

    def blink():
        toggle_eyes()
        root.after(250, toggle_eyes)
        root.after(3000, blink)
            
    def toggle_left_eye():
        current_color = c.itemcget(eye_left, 'fill')
        new_color = c.body_color if current_color == 'white' else 'white'
        current_state = c.itemcget(pupil_left, 'state')
        new_state = NORMAL if current_state == HIDDEN else HIDDEN
        c.itemconfigure(pupil_left, state=new_state)
        c.itemconfigure(eye_left, fill=new_color)
            
    def wink(event):
        toggle_left_eye()
        root.after(250, toggle_left_eye)
            
    def toggle_pupils():
        if not c.eyes_crossed:
            c.move(pupil_left, 10, -5)
            c.move(pupil_right, -10, -5)
            c.eyes_crossed = True
        else:
            c.move(pupil_left, -10, 5)
            c.move(pupil_right, 10, 5)
            c.eyes_crossed = False
            
    def toggle_tongue():
        if not c.tongue_out:
                c.itemconfigure(tongue_tip, state=NORMAL)
                c.itemconfigure(tongue_main, state=NORMAL)
                c.tongue_out = True
        else:
                c.itemconfigure(tongue_tip, state=HIDDEN)
                c.itemconfigure(tongue_main, state=HIDDEN)
                c.tongue_out = False
                
    def cheeky(event):
        toggle_tongue()
        toggle_pupils()
        hide_happy(event)
        root.after(1000, toggle_tongue)
        root.after(1000, toggle_pupils)
        return

    def show_happy(event):
        if (20 <= event.x <= 350) and (20 <= event.y <= 350):
            c.itemconfigure(cheek_left, state=NORMAL)
            c.itemconfigure(cheek_right, state=NORMAL)
            c.itemconfigure(mouth_happy, state=NORMAL)
            c.itemconfigure(mouth_normal, state=HIDDEN)
            c.itemconfigure(mouth_sad, state=HIDDEN)
            c.happy_level = 10
        return 

    def hide_happy(event):
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=NORMAL)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        return

    def sad():
        if c.happy_level == 0:
            c.itemconfigure(mouth_happy, state=HIDDEN)
            c.itemconfigure(mouth_normal, state=HIDDEN)
            c.itemconfigure(mouth_sad, state=NORMAL)
        else:
            c.happy_level -= 1
        root.after(5000, sad)
            
    def feed(event):
        if c.hunger_level < 10:
            c.hunger_level += 1
            c.itemconfigure(mouth_happy, state=NORMAL)
            root.after(500, hide_happy, event)   
        else: 
            return

    poop_logs = []

    def poop():
        if c.hunger_level == 3 or c.hunger_level == 7:

            x1 = 340 + len(poop_logs) * 10
            x2 = 380 + len(poop_logs) * 10
            poop_log = c.create_oval(x1, 380, x2, 360, fill='#663300')
            poop_logs.append(poop_log)
            c.isDirty = True
        root.after(5000, poop)

    def clean(event):
        if c.isDirty == True:
            for poop_log in poop_logs:
                c.delete(poop_log)
            c.isDirty = False
            poop_logs.clear()
            c.itemconfigure(show_happy)
            c.itemconfigure(mouth_happy, state=NORMAL)
            root.after(500, hide_happy, event)
            c.happy_level += 5
        else: return

    def hunger():
        if c.hunger_level <= 10:
            c.hunger_level -= 1
            root.after(5000, hunger)
            
    def close_game():
        global root
        root.destroy()
        root = None

    c = Canvas(root, width=400, height=400)
    c.configure(bg='dark blue', highlightthickness=0)
    c.body_color = 'purple'
    body = c.create_oval(35, 20, 365, 360, outline=c.body_color, fill=c.body_color)
    ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
    ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

    foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)
    foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)

    eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
    pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
    eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
    pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

    mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL) 
    mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
    mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
    tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
    tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

    cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
    cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
            
    def starved():
        if c.hunger_level <= 3:
            body_color = 'red'
        root.after(5000, starved)

    c.pack()

    c.bind('<Motion>', show_happy)
    c.bind('<Leave>', hide_happy)
    c.bind('<Double-1>', cheeky)

    c.happy_level = 10
    c.eyes_crossed = False
    c.tongue_out = False
    c.hunger_level = 10
    c.isDirty = False
    c.poop_count = 0

    button1 = tkinter.Button(root, text="Wink")
    button1.bind('<Button-1>', wink)
    button1.pack(pady=5)

    button2 = tkinter.Button(root, text="Feed")
    button2.bind('<Button-1>', feed)
    button2.pack(pady=5)

    button3 = tkinter.Button(root, text="Clean")
    button3.bind('<Button-1>', clean)
    button3.pack(pady=5)

    root.after(1000, starved)
    root.after(1000, poop)
    root.after(1000, blink)
    root.after(5000, sad)
    root.after(1000, hunger)
    root.mainloop()
    root.protocol("WM_DELETE_WINDOW", close_game)

if __name__ == "__main__":
    start_game()
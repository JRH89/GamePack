from turtle import *
def start_game():
    from random import choice, random
    from freegames import vector
    import tkinter as tk
    import turtle
    
    is_paused = True
    
    def pause():
        
        write("Player 1: W (up), S (down)\n\nPlayer 2: I (up), K (down)", font=("Arial", 16, "normal"))
    
    def toggle_pause():
            nonlocal is_paused
            is_paused = not is_paused
            pause()
            
    onkey(toggle_pause, key='space')
    
    root = tk.Tk()
    root.withdraw()
    
    def on_closing():
        turtle.done()
        root.destroy()
        
    root.protocol("WM_DELETE_WINDOW", on_closing)
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title("Ping-Pong")  
    
    window_width = 420
    window_height = 420
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    

    def value():
        """Randomly generate value between (-5, -3) or (3, 5)."""
        return (3 + random() * 2) * choice([1, -1])


    ball = vector(0, 0)
    aim = vector(value(), value())
    state = {1: 0, 2: 0}


    def move(player, change):
        """Move player position by change."""
        state[player] += change


    def rectangle(x, y, width, height):
        """Draw rectangle at (x, y) with given width and height."""
        up()
        goto(x, y)
        pencolor('yellow')
        fillcolor('yellow')
        down()
        begin_fill()
        for count in range(2):
            forward(width)
            left(90)
            forward(height)
            left(90)
        end_fill()


    def draw():
        """Draw game and move pong ball."""
        nonlocal is_paused
        
        if not is_paused:
            clear()
            rectangle(-200, state[1], 10, 50)
            rectangle(190, state[2], 10, 50)

            ball.move(aim)
            x = ball.x
            y = ball.y

            up()
            goto(x, y)
            color('hotpink')
            dot(10)
            update()

            if y < -200 or y > 200:
                aim.y = -aim.y

            if x < -185:
                low = state[1]
                high = state[1] + 50

                if low <= y <= high:
                    aim.x = -aim.x
                else:
                    return

            if x > 185:
                low = state[2]
                high = state[2] + 50

                if low <= y <= high:
                    aim.x = -aim.x
                else:
                    return
            
        ontimer(draw, 50)


    setup(420, 420, int(screen_width/2 - window_width / 2), int(screen_height/2 - window_height / 2))
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: move(1, 20), key='w')
    onkey(lambda: move(1, -20), key='s')
    onkey(lambda: move(2, 20), key='i')
    onkey(lambda: move(2, -20), key='k')
    draw()
    pause()
    is_paused = True
    done()
    root.mainloop()
    
if __name__ == "__main__":
    start_game()
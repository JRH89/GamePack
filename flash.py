from turtle import *
def start_game():
    from random import choice
    from time import sleep
    from freegames import floor, square, vector
    import turtle
    import tkinter as tk
    
    root = tk.Tk()
    root.withdraw()
    
    window_width = 420
    window_height = 420
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    
    def on_closing():
        turtle.done()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    turtle.TurtleScreen._RUNNING = True
    
    screen = turtle.Screen()
    screen.title("Flash Memory")
    
    pattern = []
    guesses = []
    tiles = {
        vector(0, 0): ('red', 'dark red'),
        vector(0, -200): ('blue', 'dark blue'),
        vector(-200, 0): ('green', 'dark green'),
        vector(-200, -200): ('yellow', 'khaki'),
    }

    def grid():
        """Draw grid of tiles."""
        square(0, 0, 200, 'dark red')
        square(0, -200, 200, 'dark blue')
        square(-200, 0, 200, 'dark green')
        square(-200, -200, 200, 'khaki')
        update()

    def flash(tile):
        """Flash tile in grid."""
        glow, dark = tiles[tile]
        square(tile.x, tile.y, 200, glow)
        update()
        sleep(0.5)
        square(tile.x, tile.y, 200, dark)
        update()
        sleep(0.5)

    def grow():
        """Grow pattern and flash tiles."""
        tile = choice(list(tiles))
        pattern.append(tile)

        for tile in pattern:
            flash(tile)

        print('Pattern length:', len(pattern))
        guesses.clear()

    def tap(x, y):
        """Respond to screen tap."""
        onscreenclick(None)
        x = floor(x, 200)
        y = floor(y, 200)
        tile = vector(x, y)
        index = len(guesses)

        if tile != pattern[index]:
            exit()

        guesses.append(tile)
        flash(tile)

        if len(guesses) == len(pattern):
            grow()

        onscreenclick(tap)

    def start(x, y):
        """Start game."""
        grow()
        onscreenclick(tap)

    setup(420, 420, int(screen_width/2 - window_width / 2), int(screen_height/2 - window_height / 2))
    hideturtle()
    tracer(False)
    grid()
    onscreenclick(start)
    done()
    root.mainloop()
    
if __name__ == "__main__":
    start_game()
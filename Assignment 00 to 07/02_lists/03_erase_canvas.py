from tkinter import Tk, Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 20
ERASER_SIZE = 20

def erase_objects(event):
    x, y = event.x, event.y
    items = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    for item in items:
        if item != eraser:
            canvas.itemconfig(item, fill="white")

def main():
    global canvas, eraser
    
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    
    # Create grid
    for x in range(0, CANVAS_WIDTH, CELL_SIZE):
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="blue")
    
    # Create eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")
    
    # Bind mouse movement
    canvas.bind("<B1-Motion>", erase_objects)
    canvas.bind("<Motion>", lambda e: canvas.coords(eraser, e.x, e.y, e.x + ERASER_SIZE, e.y + ERASER_SIZE))

    time.sleep(0.1)
    
    root.mainloop()

if __name__ == "__main__":
    main()
#generate apples randomly across the board
#apples cannot be where the snake is
#the board will be x by y dimensions
#use tkinter to create gui

import tkinter as tk
import Board
import PIL

class Start_screen:
    def __init__(self,root, length, width, photo_location_path):
        #length and width in pixels
        self.root = root
        self.root.wm_title("Start")

        #root contains everything so we want to place buttons and lines inside the root I think the root creates the first window

        self.length = length
        self.width = width

        #.pack() is a tool for placing the canvas frame label
        self.canvas = tk.Canvas(self.root, height = self.length, width = self.width)
        self.canvas.pack()

        background_image = tk.PhotoImage(file = photo_location_path)
        #actual image
        background_label = tk.Label(self.canvas, image = background_image)
        #uses image as a label
        background_label.place(relwidth = 1, relheight = 1)



        #.place() is a better tool for placing canvas frame or label
        self.frame = tk.Frame(self.root, bg = '#80c1ff')
        #puts a frame in the screen like a rectangle in the middle of the screen
        #also a container we can put things in our frame
        self.frame.place(relx = .2, rely = .1, relwidth = .5, relheight = .3)



        #self.label = tk.Label(self.frame, text = 'Press the start button to start', bg = 'yellow')
        #you can type in the labels
        #self.label.pack(side = 'bottom', fill = 'y', expand = True)



        self.button = tk.Button(self.frame, text = 'Start', bg = 'gray', fg = 'black', command = lambda:[self.root.destroy(), self.switchscreen()])
        #self.quit_button = tk.Button(self.frame, text = 'Quit', bg = 'gray', fg = 'black', command = self.root.destroy)
        self.button.place(relx = .3, rely = .3, relwidth = .4, relheight = .4)
        #self.quit_button.place(relx = .1, rely = .1, relwidth = .1, relheight = .1)



        #self.entry = tk.Entry(self.frame, bg = 'green')
        #self.entry.pack()

        root.mainloop()
        #runs the window

    def switchscreen(self):
        #creates instance of board and starts the game
        Board.Board(self.length, self.width)


root = tk.Tk()
length = 800
width = 800
image_location = '/Users/charliehe/Documents/Snake Game/IMG_3329.png'
new_start_screen = Start_screen(root, length, width,image_location) #fill these in later

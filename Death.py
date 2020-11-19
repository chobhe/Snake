import tkinter as tk
import Board
from PIL import ImageTk, Image

#use lauren picture as death image LOL then replace Lauren picture
#'/Users/charliehe/Documents/Snake Game/Lauren_face.png'
#option to restart or quit

def organize_scores(list):
    for x in range(1,len(list)):
        for y in range(x-1,-1,-1):
            if list[y+1]>list[y]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp
scores = []

class DeathScreen:
    def __init__(self, score):
        self.root = tk.Toplevel()
        self.root.wm_title("Death")

        self.canvas = tk.Canvas(self.root, height = 300, width = 300)
        self.canvas.pack()

        self.scores = scores
        self.scores.append(score)
        organize_scores(self.scores)


        background_image = Image.open('/Users/charliehe/Documents/Snake Game/Lauren_face.png')
        background_label = background_image.resize((300,300),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(background_label)
        self.canvas.create_image(0, 0, anchor = 'nw', image = self.background, state = 'normal')

        self.display_scores(self.scores)

        self.restart_button = tk.Button(self.canvas, text = 'Restart', bg = '#45ba8f', fg = 'black', command = lambda:[self.root.quit(), self.switchscreen()])
        #self.quit_button = tk.Button(self.frame, text = 'Quit', bg = '#145beb', fg = 'black', command = self.root.destroy)
        self.restart_button.place(relx = 0, rely = 0, relwidth = .3, relheight = .1)
        #self.quit_button.place(relx = .1, rely = .1, relwidth = .1, relheight = .1)

        self.root.mainloop()

    def switchscreen(self):
        #creates instance of board and starts the game
        Board.Board(800, 800)

    def display_scores(self,list):
        top_x = .7
        top_y = .7
        tk.Label(self.canvas, text = 'High Scores', bg = 'red').place(relx = top_x, rely = top_y, relwidth = .3, relheight = .05)
        for i,score in enumerate(list):
            tk.Label(self.canvas, text = '# ' + str(i+1) + ' : ' + str(score) + ' apples', bg ='light gray').place(relx = top_x, rely = top_y+.05*(i+1), relwidth = .3, relheight = .05)

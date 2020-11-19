import tkinter as tk
from PIL import ImageTk, Image


class SnakeModel:
    def __init__(self, square_width):
        self.size = square_width
        self.objects = [] # a list of tuples with objects
        self.locations = [[20,40],[20,20],[40,20]]
        self.create_head()
        self.create_parts()
        self.create_parts()
    def create_head(self):
        head_img = Image.open('/Users/charliehe/Documents/Snake Game/Chob_Head.png')
        head_img = head_img.resize((self.size,self.size),Image.ANTIALIAS)
        self.head = ImageTk.PhotoImage(head_img)
        self.objects.append(self.head)
        #self.canvas.create_image(20,40,anchor = 'sw', image = self.head, tag = 'head')

    def create_parts(self):
        body_img = Image.open('/Users/charliehe/Documents/Snake Game/IMG_1796.png')
        body_img = body_img.resize((self.size,self.size), Image.ANTIALIAS)
        self.body = ImageTk.PhotoImage(body_img)
        self.objects.append(self.body)

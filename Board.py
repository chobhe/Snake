import tkinter as tk
import random
from PIL import ImageTk, Image
import SnakeModel as sm
import Death as end_screen
class Board:
    def __init__(self, length, width):

        self.root = tk.Toplevel()
        self.root.wm_title("Game")
        self.root.geometry(str(length) + 'x' + str(width + 200))
        self.length = length
        self.width = width

        self.canvas = tk.Canvas(self.root, height = length, width = width, bg = 'black')
        self.canvas.pack()

        #generate random apples whenever the previous one gets eaten


        self.square_width = 20
        self.points = 0
        self.current_direction = 'down'

        self.score_label = tk.Label(self.root, text = 'Score : ' + str(self.points), bg = 'white')
        self.score_label.place(relx = 0, rely = .9, relwidth = 1, relheight = .1)

        self.run_program()

        self.root.mainloop()
    def create_board(self):
        self.special_dict = {}
        for x_coord in range(0, self.width, self.square_width):
            for y_coord in range(0, self.length, self.square_width):
                x1 = x_coord
                x2 = x_coord + self.square_width
                y1 = y_coord
                y2 = y_coord + self.square_width
                if x_coord==0 or y_coord ==0 or x_coord == self.width - self.square_width or y_coord == self.length - self.square_width:
                    self.special_dict[(x_coord,y_coord)] = self.canvas.create_rectangle(x1,y1,x2,y2,fill = 'black', tag = 'wall')

                self.canvas.create_rectangle(x1,y1,x2,y2)
        self.canvas.update()

    def run_program(self):
        self.create_board()

        #self.canvas.bind('<Button-1>',self.click) #testing bind with mouse clicks
        self.generate_apple()
        self.canvas.bind('<KeyPress>',self.key_click)
        self.canvas.focus_set()

        self.generate_snake()
        self.root.after(100,self.time)



    #def click(self, event):
        #apple_location = self.generate_apple()

    def collision_detection(self):
        #opens dead end screen
        #records score on dead end screen
        #write dead end screen with a parameter that can take in a current score
        below_head = self.canvas.find_enclosed(self.snake_locations[0][0], self.snake_locations[0][1], self.snake_locations[0][0]+20, self.snake_locations[0][1]+20)
        list = []
        for i in below_head:
            list.append(self.canvas.gettags(i))

    #    death_tiles = [0,self.width-self.square_width, self.length - self.square_width]
        if ('apple',) in list:
            #add part onto end with tag = 'body'
            self.points += 1
            self.snake.create_parts()
            self.snake_locations.append(self.previous_location)
            self.canvas_snake.append(self.canvas.create_image(self.previous_location[0], self.previous_location[1], anchor = 'nw', image = self.snake.objects[len(self.snake.objects)-1],tag = 'body'))
            self.canvas.delete('apple')
            self.generate_apple()

        elif ('body',) in list:
            end_screen.DeathScreen(self.points)
            self.root.destroy()
            #die
        elif (self.snake_locations[0][0], self.snake_locations[0][1]) in self.special_dict:
            end_screen.DeathScreen(self.points)
            self.root.destroy()
            #die




    def generate_apple(self):
        x = random.randint(20, self.width-20)
        y = random.randint(20, self.length-20)

        rect_x = x - x%20
        rect_y = y - y%20

        apple_img = Image.open('/Users/charliehe/Documents/Snake Game/BroccoliHead.png')
        apple_img = apple_img.resize((20,20),Image.ANTIALIAS)
        self.apple = ImageTk.PhotoImage(apple_img)
        self.canvas_apple = self.canvas.create_image(rect_x,rect_y,anchor = 'nw', image = self.apple, tag = 'apple')

    def time(self):
        self.collision_detection()
        self.move()
        self.collision_detection()
        self.score_label.config(text = 'Score : ' + str(self.points))

        #update scoreboard
        self.root.after(100,self.time)


    def generate_snake(self):
        SNAKE_DIMENSIONS = 20
        snake = sm.SnakeModel(SNAKE_DIMENSIONS)
        self.snake = snake #actual parts
        self.snake_locations = snake.locations
        head = self.canvas.create_image(20, 40, anchor = 'nw', image = self.snake.objects[0], tag = 'head')
        part1 = self.canvas.create_image(20, 20, anchor = 'nw', image = self.snake.objects[1], tag = 'body')
        part2 = self.canvas.create_image(40, 20, anchor = 'nw', image = self.snake.objects[2],tag = 'body')
        self.canvas_snake = [head, part1, part2]





    def move(self):
        X_CONST = 20
        Y_CONST = 20
        self.previous_location = []
        for i in self.snake_locations[0]:
            self.previous_location.append(i)

        if self.current_direction == 'left':
            self.snake_locations[0][0] -= X_CONST
            self.canvas.move(self.canvas_snake[0], -X_CONST, 0)
        elif self.current_direction == 'down':
            self.snake_locations[0][1] += Y_CONST
            self.canvas.move(self.canvas_snake[0], 0, Y_CONST)
        elif self.current_direction =='right':
            self.snake_locations[0][0] += X_CONST
            self.canvas.move(self.canvas_snake[0], X_CONST, 0)
        elif self.current_direction == 'up':
            self.snake_locations[0][1] -= Y_CONST
            self.canvas.move(self.canvas_snake[0], 0, -Y_CONST)

        for link_location in range(1,len(self.snake_locations)):
            current_location = self.snake_locations[link_location][:]
            self.canvas.coords(self.canvas_snake[link_location], self.previous_location)

            self.snake_locations[link_location] = self.previous_location
            self.previous_location = current_location



    def key_click(self, event):
        opposites = {'a':'right', 'd':'left', 's':'up', 'w':'down', '':'asdf'}
        if self.current_direction != opposites[event.char]:
            if event.char == 'a':
                #replace self.canvas.move with a move function instead that will move in the current direction
                # we will loop the move function every round based on the direction
                self.current_direction = 'left'
                self.move()
            elif event.char == 's':
                self.current_direction = 'down'
                self.move()
            elif event.char == 'd':
                self.current_direction = 'right'
                self.move()

            elif event.char == 'w':
                #self.canvas.move(self.substitute, 0,-y)
                self.current_direction = 'up'
                self.move()

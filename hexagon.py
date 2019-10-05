
from math import cos, sin,radians
class Hexagon():
    def __init__(self, row,col,parent, x, y, size, color):
        self.parent = parent # canvas
        self.x = x           # top left x
        self.y = y           # top left y
        self.size = size # length of a side
        self.color = color   # fill color
        self.selected = False
        self.row = row
        self.col = col

    def draw(self):
        start_x = self.x + 10
        start_y = self.y + 30
        angle = 60
        pointy = 30
        coords = []
        # self.can.create_text(50, 50, text='text')

        for i in range(6):
            end_x = start_x + self.size * cos(radians(angle * i-pointy))
            end_y = start_y + self.size * sin(radians(angle * i-pointy))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y
        newcoord = self.parent.create_polygon(coords[0][0],
                                    coords[0][1], 
                                    coords[1][0], 
                                    coords[1][1],
                                    coords[2][0],
                                    coords[2][1],
                                    coords[3][0],
                                    coords[3][1],
                                    coords[4][0],
                                    coords[4][1], 
                                    coords[5][0],
                                    coords[5][1], 
                                    fill=self.color,
                                    outline="gray")
    #     # print(coords)

    def draw_coordinate(self,x,y,row,col):
        self.parent.create_text(x + 1,y + 1,text='(' + row + ',' + col + ')')

    def convert_coordinate(self, x, y, row, col):
        self.parent.create_text(x,y,text='(' + row + ',' + chr(col) + ')')
     #   print('(' + row + ',' + chr(col+97) + ')')


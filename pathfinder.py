from PIL import Image
import random

class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def total_lines(self):
        with open("elevation_small.txt") as textfile:
            line_total = 0
            for lines in textfile:
                line_total +=1
        return line_total        

class Mapdata:
    def __init__(self, master_list): 
        self.master_list = master_list
        self.max_value = self.get_max()
        self.min_value = self.get_min()
    def row(self):
        return len(self.master_list[0])
    def column(self):
        return len(self.master_list)
    def color_value(self, row, column):
        color_value = int((self.max_value - self.min_value) / 256)
        return int((self.data_file[row] [column] - self.min_value) / color_value)
    def min_value(self):
        min_values = []
        with open ("elevation_small.txt") as textfile:
            coordinate = [line.split() for line in textfile]
        for y in range(self.height):
            for x in range(self.width):
                if int(coordinate [y] [x]) <= min_values:
                    min_values = int(coordinate[y][x])          
        return min_values
    def max_value(self):
        max_values = []
        with open ("elevation_small.txt") as textfile:
            coordinate = [line.split() for line in textfile]
        for y in range(self.height):
            for x in range(self.width):
                if int(coordinate[y][x]) >= max_values:
                    max_values = int(coordinate [y] [x])
        return max_values
    def create(self):

        pathfinder_map = Image.new('RGBA', (self.width, self.height))
        difference = self.max_value() -self.min_value()
        adjust_color = 255 / difference
        min_value = self.min_value()

        with open("elevation small_txt") as textfile:
            coordinate = [line.split() for line in textfile]
        for y in range(self.height):
            for x in range(self.width):
                value = int(((int(coordinate [y] [x]) - min_value) * adjust_color))
                pathfinder_map.putpixel ((x,y), (value, value, value))
       
        new_y = 300
        current_step = int((coordinate[new_y] [0]))
        x = 1

        for x in range(self.width):
            y_above = new_y -1
            y_middle = new_y
            y_below = new_y + 1
            step_above = abs(int(coordinate[y_above] [x]) - current_step)
            step_middle = abs (int(coordinate[y_middle] [x]) - current_step)
            step_below = abs(int(coordinate[y_below] [x]) - current_step)

            if step_above < step_middle and step_above < step_below:
                pathfinder_map.putpixel ((x, y_above), (0, 250, 0))
                new_y = y_above
            elif step_middle < step_above and step_middle < step_below:
                pathfinder_map.putpixel((x, y_middle), (0, 255, 0))
                new_y = y_middle     
            current_step = int((coordinate[new_y] [x]))


elevation_map = Map(600,600)
elevation_map.create()







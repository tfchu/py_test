'''
composition
X contains Y, no other object contains Y
X & Y have the same life cycle
'''
class Bitmap(object):
    '''simple class to exemplify Bitmap oepration'''
    def draw(self, x_coord, y_coord):
        '''print the coordinate to apply color to'''
        print('set color at ({}, {})'.format(x_coord, y_coord))

class Airplane(object):
    '''draw airplane in bitmap'''
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        # composition: bitmap object is initialized in constructor
        self.bitmap = Bitmap()
    def move(self, x_coord, y_coord):
        '''set x, y coordinate to draw'''
        self.x_coord = x_coord
        self.y_coord = y_coord
    def draw(self):
        '''draw color on x, y coordinate'''
        self.bitmap.draw(self.x_coord, self.y_coord)
    def __del__(self):
        print('bitmap object is closed')
        # composition: bitmap object is closed when airplane object is closed
        self.bitmap = None

def main():
    '''main function'''
    airplane = Airplane()
    airplane.move(1, 20)
    airplane.draw()

if __name__ == '__main__':
    main()

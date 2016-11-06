class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__()

    def __hash__(self):
        if(self.x + self.y == 0):
            return self.x * self.y
        return int ((self.x * self.y) / (self.x + self.y))


def move(s,c, gifted):
    if c == '^':
        house_next = Point(s.x,s.y+1)
        if(house_next not in gifted):
            gifted.add(house_next)
        s = house_next
    if c == 'v':
        house_next = Point(s.x,s.y-1)
        if(house_next not in gifted):
            gifted.add(house_next)
        s = house_next
    if c == '>':
        house_next = Point(s.x+1,s.y)
        if(house_next not in gifted):
            gifted.add(house_next)
        s = house_next
    if c== '<':
        house_next = Point(s.x-1,s.y)
        if(house_next not in gifted):
            gifted.add(house_next)
        s = house_next
    return s, gifted

def main():
    f = open("input_test", "r")
    input_str = f.read()

    santa_loc = Point(0,0)
    robot_santa_loc = santa_loc
    gifted = {santa_loc}

    i = 0
    while ( i < len(input_str) ):
        santa_loc, gifted = move(santa_loc, input_str[i], gifted)
        i += 1
        robot_santa_loc, gifted = move(robot_santa_loc, input_str[i], gifted)
        i += 1

    print len(gifted)


if __name__ == '__main__': main()
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

def main():
    f = open("input", "r")
    input_str = f.read()

    house = Point(0,0)
    gifted = {house}

    for c in input_str:
        if c == '^':
            house_next = Point(house.x,house.y+1)
            if(house_next not in gifted):
                gifted.add(house_next)
            house = house_next
            del(house_next)
        if c == 'v':
            house_next = Point(house.x,house.y-1)
            if(house_next not in gifted):
                gifted.add(house_next)
            house = house_next
            del(house_next)
        if c == '>':
            house_next = Point(house.x+1,house.y)
            if(house_next not in gifted):
                gifted.add(house_next)
            house = house_next
            del(house_next)
        if c== '<':
            house_next = Point(house.x-1,house.y)
            if(house_next not in gifted):
                gifted.add(house_next)
            house = house_next
            del(house_next)

    print len(gifted)


if __name__ == '__main__': main()
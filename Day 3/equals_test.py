"""
Sample code to understand object equality in python (coming from a Java background), and how equality is tested
among objects when using them in data structures such as Sets, or Hash Tables.
To be used in a python Set, an object needs to be hashable (https://docs.python.org/3/glossary.html#term-hashable).
If two objects are indeed different instances of a class, to define equality based on contents,
it is necessary to override the __eq__ method. To enable these objects to be used in Sets,
the __hash__ method also needs to be overridden. The contains test needs definition of equality.

The hash function needs to return an int, and this might not be the best hash function because multiple objects
can have the same hash value (multiple combinations of x and y could hash to the same value based on this function),
resulting in a relatively high collision rate which in turn defeats the purpose of using a data structure such as a
Hash Table where retrieval is O(1). However since optimal retrieval time is not the problem I am trying to solve here,
I have used this anyway.

This test should output
False
True
True
True

"""
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
        return int ((self.x * self.y) / (self.x + self.y))


def main():
    p1 = Point(1,1)
    p2 = Point(2,2)
    p3 = Point(1,1)

    print p1==p2
    print p1==p3

    points = {p1}
    points.add(p2)
    print p1 in(points)
    print p3 in (points)




if __name__ == '__main__': main()

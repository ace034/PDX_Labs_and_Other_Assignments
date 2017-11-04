# class Rectangle:
#     def __init__(self, point, top_left, height, width):
#         self.top_left = top_left
#         #top_left = (,)
#         self.p - p
#         self.height = height
#         #heith = Null
#         self.width = width
#         #width = Null
#
#     def __eq__(self, other):
#         return point1 == other.point and self.width == other.width and self.top == other.top
#
#
class Point:
    def __init__(self, x, y):
        self.x = x
        #heith = Null
        self.y = y
        #width = Null
    def distance(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        return Point(distance_x, distance_y)

#
# def comp_recs(a, b):
#     one_h = a.height
#     two_h = b.height
#     return one_h == other.point and self.width == other.width and self.top == other.top
#
# #
# # x = Point(2,3)
# # y = Point(3,4)
# # distance =
# #
# # input = ("Are you using [P]oint's or [R]ectangle?")
# # 'P' = Point()
# # 'R' = Rectangle()
#     # if p
#
#
#
# old_rec = Rectangle(1, 2, 3)
# new_rec = Rectangle(1, 2, 3)
#
# if new_rec == old_rec:
#     print('true')

class Rectangle:
    def __init__(self, top_left, width ,height):
        self.top_left = top_left
        #top_left = (,)
        self.height = height
        #heith = Null
        self.width = width
        #width = Null

    def area(self):
        area = self.height * self.width
        return area

    def contains(self, point):
        return (self.top_left.x <= point.x <= self.top_left.x + self.width and
            self.top_left.y <= point.y <= self.top_left.y + self.height)

new_inst = Rectangle(Point(2,3), 5, 7)
sec_inst = Rectangle(Point(2,3), 5, 7)

print(new_inst.contains(Point(4,6)))

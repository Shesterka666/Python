class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def lenght(self,newp):
        return((self.x-newp.x)**2 + (self.y - newp.y)**2)**0.5

class Rectangle:
    def __init__(self, p1: tuple =(0.,0.), p2: tuple = (1.,1.)):
        self.lt = Point(*p1)#lt = left top
        self.rb = Point(*p2)#rb = right bottom
        self.lb = Point(self.lt.x,self.rb.y)
        self.rt = Point(self.rb.x,self.lt.y)
    
    def side_a(self):
        return self.lt.lenght(self.rt)
    
    def side_b(self):
        return self.lt.lenght(self.lb)
    
    def perimeter(self, cd=2):
        return round(2*(self.side_a()+ self.side_b()),cd)

    def area(self,cd =2):
        return round(self.side_a()*self.side_b(),cd)       

    def get_pos(self,cd =2):#я сделал наоборт случайно :) для меня это левая нижняя :(
        return (round(self.lb.x,cd), round(self.lb.y,cd))
    
    def get_size(self,cd =2):
        return (round(self.side_a(),cd),round(self.side_b(),cd))

    def move(self,x,y):
        self.lt.x += x
        self.lt.y += y
        self.lb.x += x
        self.lb.y += y
        self.rt.x += x
        self.rt.y += y
        self.rb.x += x
        self.rb.y += y
    
    def resize(self,width, height):
        #side_a = 
        da = self.side_a() - width
        db = self.side_b() - height
        self.lb.y += da
        self.rt.x += db
        self.rb.x += db
        self.rb.y += da

if __name__ == "__main__":
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    #print(rect.perimeter())
    #print(rect.area())
    print(rect.get_pos(), rect.get_size())
    rect.move(1.32, -5)
    print(rect.get_pos(), rect.get_size())
    rect.resize(1.32, 5)
    print(rect.get_pos(), rect.get_size())



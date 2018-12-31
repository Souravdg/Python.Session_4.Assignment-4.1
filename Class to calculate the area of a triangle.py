#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Polygon():
    def __init__(self,lstPoly):
        self.lst = lstPoly
        self.a = lstPoly[0]
        self.b = lstPoly[1]
        self.c = lstPoly[2]

    #calculate the semi-perimeter
    def semiperimeter(self):
        sum = 0
        for x in range(len(self.lst)):
            sum = sum + self.lst[x]
        return (sum/2)

    
class Triangle(Polygon):
    def __init__(self,lstTriangle):
        Polygon.__init__(self,lstTriangle)
        
    #calculate the area
    def area(self):
        s=self.semiperimeter()
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return ("The area of the triangle is %f" %(area))
    
        
lst = [4,6,3]
mytriangle = Triangle(lst)
area = mytriangle.area()
print(area)


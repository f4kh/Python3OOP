'''
Created on Feb 16, 2019

@author: fakhri
'''

class Point:
    pass



#2 objects
p1 = Point()
p2 = Point()

#we do not need to declare attributes in class in advance like other oop languagges java 4exp . :)
p1.x = 2
p1.y = 4
p1.z = 6

p2.x = 1
p2.y = 3
p2.z = 5

#address of object in memory
print(p1)
print(p1.x,p1.y,p1.z)
print(p2) 
print(p2.x,p2.y,p2.z)
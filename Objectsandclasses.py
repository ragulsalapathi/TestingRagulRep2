# ratings = [20,2,8,6,4,10,16,18,12]
# ratings.sort()
# print(ratings)
# ratings.reverse()
# print(ratings)
# class car:
#     max_speed = 120

#     def __init__(self,make,model,color,speed=0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.speed = speed
import matplotlib.pyplot as plt

class Circle(object):
    def __init__(self,radius=3,color='green'):
        self.radius = radius
        self.color = color

#     def add_radius(self,r):
#         self.radius=self.radius+r
#         return self.radius
    
#     def drawcircle(self):
#         plt.gca().add_patch(plt.Circle((0,0),radius=self.radius,fc=self.color))
#         plt.axis('scaled')
#         plt.show()

# # class Circle(object):
# #     # Constructor
# #     def __init__(self, radius=3, color='blue'):
# #         self.radius = radius
# #         self.color = color 
    
# #     # Method
# #     def add_radius(self, r):
# #         self.radius = self.radius + r
# #         return self.radius
    
# #     # Method
# #     def drawCircle(self):
# #         plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
# #         plt.axis('scaled')
# #         plt.show()

# # ✅ Create a circle object and use it
# c = Circle(radius=0, color='red')
# print("Initial radius:", c.radius)

# # ✅ Add more radius
# c.add_radius(1)
# print("New radius:", c.radius)

# # ✅ Draw the circle
# c.drawcircle()


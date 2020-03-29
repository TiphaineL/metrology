#from Bezier.math_toolbox import bezier_function, arc_length,bezier_curvature
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

##############################################################################
def vector_length(vector):
    return np.sqrt(sum(element ** 2 for element in vector))

def binomial(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def bezier_function_1D(curve):

    bezier_function = 0
    dummy = np.arange(start=0, stop=1, step=1e-3)

    for n in range(curve.order + 1):
        bezier_order_n = binomial(curve.order, n) * (1 - dummy) ** (curve.order - n) \
                           * dummy ** (n) * curve.points[n]
        bezier_function += bezier_order_n
    return bezier_function

def bezier_function(curve):

    bezier_function = []

    for d in range(curve.dimension):

        points_in_1d = curve.points[:,d]
        bezier_function.append(bezier_function_1D(Bezier_curve(points_in_1d)))

    return bezier_function

def points_derivative(order, points):
    derivated_points = []
    for i in range(order):
        derivated_points.append((order) * (points[i + 1] - points[i]))

    return np.array(derivated_points)

def arc_length(order, control_points):

    bezier_derivative = Bezier_curve(points_derivative(order, control_points))

    curve_derivative = bezier_derivative.function()

    squared_sum = 0
    for curve_along_one_dimension in curve_derivative:
        squared_sum = + curve_along_one_dimension ** 2

    return sum(np.sqrt(squared_sum)) / len(np.sqrt(squared_sum))

def bezier_curvature(order,control_points):

    derivative_1st_order = Bezier_curve(points_derivative(order,control_points))
    derivative_2nd_order = Bezier_curve(points_derivative(derivative_1st_order.order,derivative_1st_order.points))

    return vector_length(np.cross(derivative_1st_order.function(), derivative_2nd_order.function())) \
           / (vector_length(derivative_1st_order.function())) ** 3

##########################################

class Bezier_curve:

    def __init__(self,control_points):
        self.points = control_points
        self.order = control_points.shape[0] - 1

        if len(control_points.shape) > 1:
            self.dimension = control_points.shape[1]
        else:
            self.dimension = 1

    def function(self):
        return bezier_function(self)

    def arc_length(self):
        return arc_length(self.order, self.points)

    def curvature(self):
        return bezier_curvature(self.order,self.points)

    def plot(self):

        fig = plt.figure(1)

        if self.dimension == 1:
            plt.plot(self.function())

        elif self.dimension == 2:
            plt.plot(self.function()[0], self.function()[1])

        elif self.dimension == 3:
            for i in range(3):
                ax = fig.add_subplot(111, projection='3d')
                ax.plot(self.function()[0], self.function()[1], self.function()[2])
        else:
            print('No plotting for dimension > 3')

points = np.array([[ 105., -45.45, 0.],
                   [ 105., -45.45, 9858.32126428],
                   [ 5000.,-700., 20051.12340604],
                   [ 5000., -700., 30000.]])

curve = Bezier_curve(points)
print(curve.points)
print(curve.dimension)
print(curve.order)


curve.function()

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot(curve.function()[0],curve.function()[1],curve.function()[2])
# ax.set_ylim3d(-2500, 2500)
#ax.set_zlim3d(-2, 2)
ax.grid(False)
# ax.set_aspect('equal')
ax.set_xlabel('X (mm)')
ax.set_ylabel('Z (mm)')
ax.set_zlabel('Y (mm)')
# ax.view_init(-50, 280)
# ax.view_init(-45,270)
# ax.set_axis_off()
plt.show()

#curve.arc_length()
#print(curve.arc_length())
#print(curve.curvature())


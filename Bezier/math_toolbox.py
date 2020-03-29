import math
import numpy as np
import Bezier_classes

def vector_length(vector):
    return np.sqrt(sum(element**2 for element in vector))

def binomial(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def bezier_function_1D(order, control_points):
    
    bezier_function = 0
    dummy = np.arange(start=0, stop=1, step=1e-6)
    
    for i in range(order+1):
        parametric_curve = binomial(order, i) * (1 - dummy) ** (order - i) \
                           * dummy ** (i) * control_points[i]
        bezier_function += parametric_curve
        
    return bezier_function

def bezier_function(order, dimension, control_points):

    bezier_function = []

    for d in range(dimension):
        points_in_1d = control_points[:, d]
        bezier_function.append(bezier_function_1D(order, points_in_1d))

    return bezier_function

def points_derivative(order, points):

    derivated_points = []
    for i in range(order):
        derivated_points.append((order) * (points[i + 1] - points[i]))

    return np.array(derivated_points)

def arc_length(order, control_points):

    bezier_derivative = Bezier_classes.Bezier_curve(points_derivative(order, control_points))

    curve_derivative = bezier_derivative.function()

    squared_sum = 0
    for curve_along_one_dimension in curve_derivative:
        squared_sum = + curve_along_one_dimension ** 2

    return sum(np.sqrt(squared_sum)) / len(np.sqrt(squared_sum))

def bezier_curvature(control_points):

    derivative_1st_order = Bezier_curve(points_derivative(control_points)).function
    derivative_2nd_order = Bezier_curve(points_derivative(points_derivative(control_points))).function

    return vector_length(np.cross(derivative_1st_order, derivative_2nd_order)) \
           / (vector_length(derivative_1st_order)) ** 3

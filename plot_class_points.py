import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

from plot_points import plot_points

class_point_num = 30
dim_num = 2


def plot_class_points():
    first_class_pts = np.fromfile('first.bin')
    first_class_pts.shape = (class_point_num, dim_num)
    second_class_pts = np.fromfile('second.bin')
    second_class_pts.shape = (class_point_num, dim_num)
    third_class_pts = np.fromfile('third.bin')
    third_class_pts.shape = (class_point_num, dim_num)
    class_points = []
    class_points.append(first_class_pts)
    class_points.append(second_class_pts)
    class_points.append(third_class_pts)
    
    plot_points(class_points, [], 'class_points.png')

if __name__ == '__main__':
    plot_class_points()

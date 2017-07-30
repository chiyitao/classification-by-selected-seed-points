import matplotlib
matplotlib.use('Agg')


import numpy as np
import matplotlib.pyplot as plt



from seed_point import seed_point, dst_point_set

from plot_points import plot_points

# constant
max_coord = 200 # inherit from the previous random_gen file
class_point_num = 30
seed_point_num = 100
dim_num = 2

# read every class points
first_class_points = np.fromfile('first.bin', dtype=np.float)
first_class_points.shape = (class_point_num, dim_num)
# for pt in first_class_points:
#     print pt

second_class_points = np.fromfile('second.bin', dtype=np.float)
second_class_points.shape = (class_point_num, dim_num)
# for pt in second_class_points:
#     print pt

third_class_points = np.fromfile('third.bin', dtype=np.float)
third_class_points.shape = (class_point_num, dim_num)
# for pt in third_class_points:
#     print pt

# generate seed for boundary plane
seed_pts = max_coord * np.random.rand(seed_point_num, dim_num)
# calculate the corresponding distance
seed_pts_rslt = []
for i in range(0, len(seed_pts)):
    spt = seed_point(seed_pts[i])
    # first
    first_class_dst_pt_set = dst_point_set(0, first_class_points)
    spt.calc_dists(first_class_dst_pt_set)
    # second
    second_class_dst_pt_set = dst_point_set(1, second_class_points)
    spt.calc_dists(second_class_dst_pt_set)
    # third
    third_class_dst_pt_set = dst_point_set(2, third_class_points)
    spt.calc_dists(third_class_dst_pt_set)

# select seed point that has equivalent distance to all the classes.




# plot
classes_points = []
classes_points.append(first_class_points)
classes_points.append(second_class_points)
classes_points.append(third_class_points)
print 'len of classes_points = {len_classes_points}'.format(len_classes_points = len(classes_points))
plot_points(classes_points, seed_pts)

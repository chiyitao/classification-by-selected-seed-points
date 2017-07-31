import matplotlib
matplotlib.use('Agg')


import numpy as np
import matplotlib.pyplot as plt



from seed_point import seed_point, dst_point_set

from plot_points import plot_points

from selecting_seed_points import selecting_seed_points

from min_and_max import min_and_max

# constant
max_coord = 200 # inherit from the previous random_gen file
class_point_num = 30
seed_point_num = 200
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

# basic_points
classes_points = []
classes_points.append(first_class_points)
classes_points.append(second_class_points)
classes_points.append(third_class_points)



# generate seed for boundary plane in given range
min_and_max_x_y = min_and_max(classes_points)

# LIMITATION: for 2-dimension points
seed_xs = min_and_max_x_y[0] + (min_and_max_x_y[2] - min_and_max_x_y[0]) * np.random.rand(seed_point_num, 1)
seed_ys = min_and_max_x_y[1] + (min_and_max_x_y[3] - min_and_max_x_y[1]) * np.random.rand(seed_point_num, 1)

seed_pts = []
for i in range(0, len(seed_xs)):
    seed_pts.append((seed_xs[i][0], seed_ys[i][0]))
    # print (seed_xs[i])
    # print (seed_ys[i])


# seed_pts = max_coord * np.random.rand(seed_point_num, dim_num)

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
    # save the caclulated seed_point in the list
    seed_pts_rslt.append(spt)




# select seed point that has equivalent distance to all the classes.
index_and_divided_pairs = selecting_seed_points(seed_pts_rslt)



for i in range(0, len(classes_points)): # TODO: class_num should calculated first
    for j in range(i+1, len(classes_points)):
        cur_index_and_pairs_points = []
        for k in range(0, len(index_and_divided_pairs)):
            if (i, j) == index_and_divided_pairs[k][1]: # equivalent to divided class pair
                cur_index_and_pairs_points.append(seed_pts_rslt[index_and_divided_pairs[k][0]].coord)
            # plot

        # debug cur_index_and_pairs_points
        for pt in cur_index_and_pairs_points:
            print pt
            
        plot_points(classes_points, cur_index_and_pairs_points, '{i}_{j}.png'.format(i=i, j=j))
            





# drawing the debugging dividing points



# plot
# print 'len of classes_points = {len_classes_points}'.format(len_classes_points = len(classes_points))
# plot_points(classes_points, seed_pts)

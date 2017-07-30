# import cv2

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


# const
max_coord = 200
min_dist = 40 # use standard of Euclidean distance
delta_dist = 15
class_point_num = 30
dim_num = 2


# first center
first_center = max_coord * np.random.rand(1, dim_num)



# second center
second_center = []
while True:
    second_center = max_coord * np.random.rand(1, dim_num)
    sec_to_fst_dist_square = ((second_center - first_center)[0][0] * (second_center - first_center)[0][0] + \
                              (second_center - first_center)[0][1] * (second_center - first_center)[0][1])
    if sec_to_fst_dist_square > min_dist * min_dist:
        break


    
# third_center
third_center = []
while True:
    third_center = max_coord * np.random.rand(1, dim_num)
    thd_to_fst_dist_square = ((third_center - first_center)[0][0] * (third_center - first_center)[0][0] + \
                              (third_center - first_center)[0][1] * (third_center - first_center)[0][1])

    thd_to_sec_dist_square = ((third_center - second_center)[0][0] * (third_center - second_center)[0][0] + \
                              (third_center - second_center)[0][1] * (third_center - second_center)[0][1])

    
    if (thd_to_fst_dist_square > min_dist * min_dist) and (thd_to_sec_dist_square > min_dist * min_dist):
        break



# generate classes points
first_class_start = ((first_center[0][0] - delta_dist), (first_center[0][1] - delta_dist))
first_class_points = first_class_start + 2 * delta_dist * np.random.rand(class_point_num, dim_num)

print 'first_center = {first_center}'.format(first_center=first_center)
print 'first_class_points = \n'
print first_class_points

first_class_points_file = open('first.txt', 'wb')
first_class_points_file.write(first_class_points)
first_class_points_file.close()

second_class_start = ((second_center[0][0] - delta_dist), (second_center[0][1] - delta_dist))
second_class_points = second_class_start + 2 * delta_dist * np.random.rand(class_point_num, dim_num)

print 'second_center = {second_center}'.format(second_center=second_center)
print 'second_class_points = \n'
print second_class_points
second_class_points_file = open('second.txt', 'wb')
second_class_points_file.write(second_class_points)
second_class_points_file.close()


third_class_start = ((third_center[0][0] - delta_dist), (third_center[0][1] - delta_dist))
third_class_points = third_class_start + 2 * delta_dist * np.random.rand(class_point_num, dim_num)

print 'third_center = {third_center}'.format(third_center=third_center)
print 'third_class_points = \n'
print third_class_points
third_class_points_file = open('third.txt', 'wb')
third_class_points_file.write(third_class_points)
third_class_points_file.close()


# plot

first_class_x_array = []
first_class_y_array = []
for pt in first_class_points:
    first_class_x_array.append(pt[0])
    first_class_y_array.append(pt[1])

second_class_x_array = []
second_class_y_array = []
for pt in second_class_points:
    second_class_x_array.append(pt[0])
    second_class_y_array.append(pt[1])

third_class_x_array = []
third_class_y_array = []
for pt in third_class_points:
    third_class_x_array.append(pt[0])
    third_class_y_array.append(pt[1])


min_x = np.min([np.min(first_class_x_array), np.min(second_class_x_array), np.min(third_class_x_array)])
min_y = np.min([np.min(first_class_y_array), np.min(second_class_y_array), np.min(third_class_y_array)])
max_x = np.max([np.max(first_class_x_array), np.max(second_class_x_array), np.max(third_class_x_array)])
max_y = np.max([np.max(first_class_y_array), np.max(second_class_y_array), np.max(third_class_y_array)])

actual_min_x = np.floor(min_x / 10) * 10
actual_min_y = np.floor(min_y / 10) * 10
actual_max_x = np.ceil(max_x / 10) * 10
actual_max_y = np.ceil(max_y / 10) * 10

x_ticks = np.arange(actual_min_x, actual_max_x, 10)
y_ticks = np.arange(actual_min_y, actual_max_y, 10)


plt.figure(figsize=((actual_max_x - actual_min_x) / 10, (actual_max_y - actual_min_y) / 10))
plt.axis([actual_min_x, actual_max_x, actual_min_y, actual_max_y])

plt.xticks(x_ticks)
plt.yticks(y_ticks)

axes = plt.subplot(111)

type1 = axes.scatter(first_class_x_array, first_class_y_array, c='red')
type2 = axes.scatter(second_class_x_array, second_class_y_array, c='green')
type3 = axes.scatter(third_class_x_array, third_class_y_array, c='blue')

plt.savefig('points.png')

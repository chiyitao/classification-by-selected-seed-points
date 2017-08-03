import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.lines import Line2D

# constant for colors
class_colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange'] # TODO: more colors

def plot_points(class_arrays, seed_points, image_name):
    class_x_array = [] # two dimensions
    class_y_array = [] # two dimensions    

    # print 'len of class_arrays = {len_class_arrays}'.format(len_class_arrays = len(class_arrays))
    # store point pairs in class_x_array and class_y_array
    for i in range(0, len(class_arrays)):
        class_x_array.append([]) # prepare to append x value
        class_y_array.append([]) # prepare to append y value
        
        for pt in class_arrays[i]:
            class_x_array[i].append(pt[0])
            class_y_array[i].append(pt[1])

    # seed_point
    seed_point_x_array = []
    seed_point_y_array = []
    for i in range(0, len(seed_points)):
        seed_point_x_array.append(seed_points[i][0])
        seed_point_y_array.append(seed_points[i][1])

    # the min and max point
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0


    if class_arrays != []:
        # print len(class_x_array)
        for i in range(0, len(class_x_array)):
            # min_x
            arr_min_x = np.min(class_x_array[i])
            if i == 0:
                min_x = arr_min_x
            else:
                min_x = np.min([arr_min_x, min_x])
                
            # max_x
            arr_max_x = np.max(class_x_array[i])
            if i == 0:
                max_x = arr_max_x
            else:
                max_x = np.max([arr_max_x, max_x])
                
            # min_y
            arr_min_y = np.min(class_y_array[i])
            if i == 0:
                min_y = arr_min_y
            else:
                min_y = np.min([arr_min_y, min_y])
                
            # max_y
            arr_max_y = np.max(class_y_array[i])
            if i == 0:
                max_y = arr_max_y
            else:
                max_y = np.max([arr_max_y, max_y])
                
    elif seed_points !=[]:
        # min_x
        min_x = np.min(seed_point_x_array)
                
        # max_x
        max_x = np.max(seed_point_x_array)
                
        # min_y
        min_y = np.min(seed_point_y_array)
                
        # max_y
        max_y = np.max(seed_point_y_array)        



    
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

    types = []
    
    for i in range(0, len(class_x_array)):
        cur_type = axes.scatter(class_x_array[i], class_y_array[i], c=class_colors[i])

    cur_seed_type = axes.scatter(seed_point_x_array, seed_point_y_array, marker='x', c=class_colors[len(class_arrays)])
    

    plt.savefig(image_name)

def plot_lines(axes, class_pts, seed_pts, image_name):

    class_x_array = [] # two dimensions
    class_y_array = [] # two dimensions    

    
    # store point pairs in class_x_array and class_y_array
    for i in range(0, len(class_arrays)):
        class_x_array.append([]) # prepare to append x value
        class_y_array.append([]) # prepare to append y value
        
        for pt in class_arrays[i]:
            class_x_array[i].append(pt[0])
            class_y_array[i].append(pt[1])

    # seed_point
    seed_point_x_array = []
    seed_point_y_array = []
    for i in range(0, len(seed_points)):
        seed_point_x_array.append(seed_points[i][0])
        seed_point_y_array.append(seed_points[i][1])

    # the min and max point
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0


    if class_arrays != []:
        # print len(class_x_array)
        for i in range(0, len(class_x_array)):
            # min_x
            arr_min_x = np.min(class_x_array[i])
            if i == 0:
                min_x = arr_min_x
            else:
                min_x = np.min([arr_min_x, min_x])
                
            # max_x
            arr_max_x = np.max(class_x_array[i])
            if i == 0:
                max_x = arr_max_x
            else:
                max_x = np.max([arr_max_x, max_x])
                
            # min_y
            arr_min_y = np.min(class_y_array[i])
            if i == 0:
                min_y = arr_min_y
            else:
                min_y = np.min([arr_min_y, min_y])
                
            # max_y
            arr_max_y = np.max(class_y_array[i])
            if i == 0:
                max_y = arr_max_y
            else:
                max_y = np.max([arr_max_y, max_y])
                
    elif seed_points !=[]:
        # min_x
        min_x = np.min(seed_point_x_array)
                
        # max_x
        max_x = np.max(seed_point_x_array)
                
        # min_y
        min_y = np.min(seed_point_y_array)
                
        # max_y
        max_y = np.max(seed_point_y_array)        



    
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

    types = []
    
    for i in range(0, len(class_x_array)):
        cur_type = axes.scatter(class_x_array[i], class_y_array[i], c=class_colors[i])

    cur_seed_type = axes.scatter(seed_point_x_array, seed_point_y_array, marker='x', c=class_colors[len(class_arrays)])

    # drawing lines
    # for every seed in seed_pts, drawing a line to the class_pts
    for i in range(0, len(seed_pts)):
        

    plt.savefig(image_name)

    
    


if __name__ == '__main__':
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

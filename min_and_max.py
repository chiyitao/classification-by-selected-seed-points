import numpy as np

def min_and_max(class_arrays):

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


    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0


    # print len(class_x_array)
    for i in range(0, len(class_x_array)):
        # min_x
        # print len(class_x_array[i])
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
        # max_x
        arr_max_y = np.max(class_y_array[i])
        if i == 0:
            max_y = arr_max_y
        else:
            max_y = np.max([arr_max_y, max_y])

    return (min_x, min_y, max_x, max_y)

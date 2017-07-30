import numpy as np
import math

class dst_point_set():
    def __init__(self, class_index, coords):
        self.class_index = class_index
        self.coords = coords


class seed_point():
    def __init__(self, coord):
        # self.index = index # point index in the array
        self.coord = coord
        self.dist_tuples = [] # has class_num distances

    def calc_dists(self, dst_points):
        print 'self.coord = {self_coord}'.format(self_coord=self.coord)
        dists = []        
        for dst_pt in dst_points.coords:            

            # print 'dst_pt = {dst_pt}'.format(dst_pt=dst_pt)
            subtract_arr = np.array(self.coord) - np.array(dst_pt)
            cur_dist_sum = 0
            for i in range(0, len(subtract_arr)):
                cur_dist_sum += subtract_arr[i] * subtract_arr[i]                
            cur_dist = math.sqrt(cur_dist_sum) / len(subtract_arr)
            # print 'cur_dist = {cur_dist}'.format(cur_dist=cur_dist)            
            dists.append(cur_dist)
            
        # for dst in dists:
        #    print 'distance for {self_coord} is {dst}'.format(self_coord = self.coord, dst=dst)

        average_dist = np.sum(np.array(dists)) / len(dists)
        self.dist_tuples.append((dst_points.class_index, average_dist, dists))
        print 'class {class_index} has average dist of {average_dist}' \
            .format(class_index = dst_points.class_index, average_dist = average_dist)
        
if __name__ == '__main__':
    # generate dst_points
    dst_points = [[5, 5], \
                  [4, 6], \
                  [3, 7], \
                  [2, 8], \
                  [1, 9]]
    dst_pt_set = dst_point_set(0, dst_points)
    
    spts = []
    seed_num = 10
    for i in range(0, seed_num):
        spt = seed_point([i, seed_num - i])
        spts.append(spt)
        spt.calc_dists(dst_pt_set)
        

        

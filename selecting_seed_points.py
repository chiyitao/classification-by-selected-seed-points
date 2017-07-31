import numpy as np
from seed_point import seed_point

equiv_ratio = 0.05



# selecting seed points which are not belonging to any of the classes
# which have approximately equivalent distances to given two classes.



def selecting_seed_points(seed_pts_results):
    index_and_divided_pairs = []
    for k in range(0, len(seed_pts_results)):
        spt = seed_pts_results[k]
        # select two distances that are approximately equivalent
        class_num = len(spt.dist_tuples)
        for i in range(0, class_num):
            for j in range(i+1, class_num):
                min_dist = np.min([spt.dist_tuples[i][1], spt.dist_tuples[j][1]]) # average_dist
                diff_dist = np.abs(spt.dist_tuples[i][1] - spt.dist_tuples[j][1])
                if diff_dist < equiv_ratio * min_dist:                    
                    # push the result
                    index_and_divided_pairs.append([k, (i, j)])

    print 'len(index_and_divided_pairs) = {len_of_result}'.format(len_of_result=len(index_and_divided_pairs))
    return index_and_divided_pairs
                

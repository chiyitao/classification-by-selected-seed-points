import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

from plot_points import plot_points

def plot_seed_points():
    seed_pts = np.load('seed.npy')
    plot_points([], seed_pts, 'seed.png')

if __name__ == '__main__':
    plot_seed_points()

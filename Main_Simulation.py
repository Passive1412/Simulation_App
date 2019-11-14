import matplotlib.animation as animation
from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import argparse
import scipy
import time
import copy
import sys
import os


class Map:
    def __init__(self, B, S):
        self.fig = plt.figure(figsize=(7,7))
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon = True)
        self.ax.set_xlim(0, S), self.ax.set_xticks([])
        self.ax.set_ylim(0, S), self.ax.set_yticks([])
        self.scat = self.ax.scatter(B.balls['position'][:,0], B.balls['position'][:,1],
                                              s=B.balls['size']*100, lw = 0.5, edgecolors=B.balls['color'],
                                              facecolor=B.balls['color'])


class Balls:
    def __init__(self, N, V, S):
        self.balls = np.zeros(N, dtype=         [('position',  float, 2),
                                                ('velocity', float, 2),
                                                ('size', float),
                                                ('color', float, 3)])

        self.balls['size'] = np.random.uniform(1, 10, N)
        self.balls['velocity'] = np.random.uniform(-V, V, (N, 2))
        CheckPosition(self.balls['position'], self.balls['size'], S)
        CheckSize(self.balls['color'], self.balls['size'])


def CheckForLess(dist, maxval):
    if maxval <= 5:
        maxval = maxval*2
    dist = [i for i in dist if i != 0]
    return any(x < maxval for x in dist)


def CheckPosition(balls, sizes, S):
    for x, ball in enumerate(balls.tolist()):
        val = sizes[x]
        ball = np.random.uniform(0+10, S-10, (1, 2))
        balls[x] = ball
        dist = distance.cdist(ball, balls.tolist(), 'euclidean')
        if not CheckForLess(dist[0].tolist(), val):
            continue
        else:
            counter = 0
            while CheckForLess(dist[0].tolist(), val):
                counter += 1
                ball = np.random.uniform(0 + 10, S - 10, (1, 2))
                balls[x] = ball
                dist = distance.cdist(ball, balls.tolist(), 'euclidean')
                if counter >= 100:
                    continue
    return


def CheckSize(color, size):
    for x, ball in enumerate(color):
        c = size[x]
        color[x] = [1 - c / 10.0, 1 - c / 10.0, 1 - c / 10.0]


def StartInput():
    parser = argparse.ArgumentParser(description='Simulation of balls')
    parser.add_argument('-n', '--number', type=int, default=25, help='Number of balls to simulate')
    parser.add_argument('-t', '--time', type=int, default=60, help='Duration of simulation in seconds')   
    parser.add_argument('-v', '--velocity', type=int, default=10, help='Max velocity') 
    parser.add_argument('-s', '--size', type=int, default=100, help='Size of box in meters') 
    return parser.parse_args()


def update(frame_number):
    current_index = frame_number
    B.balls['position'][:,0]+=B.balls['velocity'][:,0]
    B.balls['position'][:,1]+=B.balls['velocity'][:,1]    


def main():
    args = StartInput()
    balls = Balls(args.number, args.velocity, args.size)
    map = Map(balls, args.size)
    #update(0)

    plt.show()
    
if __name__ == "__main__":
    main()

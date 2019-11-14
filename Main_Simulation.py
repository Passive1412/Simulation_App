import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import argparse
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
        self.balls = np.zeros(N, dtype=[ ('position',  float, 2),
                                                ('velocity', float, 2),
                                                ('size', float),
                                                ('color', float, 3)])
        self.balls['position']   = np.random.uniform(0+10, S-10, (N, 2))
        self.balls['velocity']   = np.random.uniform(-V, V, (N, 2))
        self.balls['size']        = np.random.uniform(0, 10, N)
        for i in range(0,N):
            c = self.balls['size'][i]
            self.balls['color'][i] = [1-c/10.0, 1-c/10.0, 1-c/10.0]

def startInput():
    parser = argparse.ArgumentParser(description='Simulation of balls')
    parser.add_argument('-n', '--number', type=int, default=10, help='Number of balls to simulate')
    parser.add_argument('-t', '--time', type=int, default=60, help='Duration of simulation in seconds')   
    parser.add_argument('-v', '--velocity', type=int, default=10, help='Max velocity') 
    parser.add_argument('-s', '--size', type=int, default=100, help='Size of box in meters') 
    return parser.parse_args()

def update(frame_number):
    current_index = frame_number
    B.balls['position'][:,0]+=B.balls['velocity'][:,0]
    B.balls['position'][:,1]+=B.balls['velocity'][:,1]    

def main():
    args = startInput()
    balls = Balls(args.number, args.velocity, args.size)
    map = Map(balls, args.size)
    update(0)

    #plt.show()
    
if __name__ == "__main__":
    main()
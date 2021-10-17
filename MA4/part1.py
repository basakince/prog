import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def part1(n):
    inCircle = 0
    total = 0
    insideX = []
    insideY = []
    outsideX = []
    outsideY = []
    for i in range(n):
        coordX = random.uniform(-1,1)
        coordY = random.uniform(-1,1)

        if (coordX*coordX + coordY*coordY) <= 1: #in circle
            inCircle += 1
            insideX.append(coordX)
            insideY.append(coordY)
        else: #out circle
            outsideX.append(coordX)
            outsideY.append(coordY)
        total += 1

    #print("---")
    print("inside the circle=",str(inCircle))
    #print(total)
    pi = (4 * inCircle) / total;
    print("approximation=",str(pi))
    #print("---")
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')
    ax.scatter(insideX, insideY, color='g',edgecolor=None)
    ax.scatter(outsideX, outsideY, color='r',edgecolor=None)
    #plt.show()
    plt.savefig('part1.png')
    
def main(args):
    print("Part1 Program is running for n="+str(args[1]))
    print("math.pi="+str(math.pi))
    part1(int(args[1]))


if __name__ == "__main__":
    main(sys.argv)
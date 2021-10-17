import sys
import random
import math
from functools import reduce
from time import perf_counter

def part2(n,d):
    inCircle = 0
    total = 0
    insideX = []
    coordX = []
    for i in range(n):
        coordX = []
        for j in range(d):
            coordX.append(random.uniform(-1,1))

        #Map() + Lamdbda  function -- new list with square of each elements
        #MAP = ikinci parametrede verilen listeye 1. parametrede yazılan fonksiyonu uygulayarak yeni bir liste döndürür
        squareList = map(lambda x: x * x, coordX)

        #functools.reduce -- sum of all elements
        sqTotal = reduce((lambda x, y: x + y), squareList)
        if (sqTotal) <= 1:
            inCircle += 1
            #insideX.append(coordX)
        total+=1
    result = (math.pow( (4 * inCircle) / total ,(d/2)) * math.pow(1,d)) / (math.gamma((d/2)+1))
    print("inside the circle=",inCircle)
    print("approximation=",result)
    
def main(args):
    time_start = perf_counter()
    print("Part2 Program is running for n="+str(args[1])+" d="+str(args[2]))
    part2(int(args[1]),int(args[2]))
    time_stop = perf_counter()
    print("Elapsed time:",  time_stop-time_start, "seconds")


if __name__ == "__main__":
    main(sys.argv)
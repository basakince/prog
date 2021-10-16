import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from time import perf_counter
import concurrent.futures as future

def getTotalInCircle(n,d):
    inCircle = 0
    total = 0
    insideX = []
    coordX = []
    for i in range(n):
        coordX = []
        for j in range(d):
            coordX.append(random.uniform(-1,1))

        #Map() + Lamdbda  function -- new list with square of each elements
        squareList = map(lambda x: x * x, coordX)

        #functools.reduce -- sum of all elements
        sqTotal = reduce((lambda x, y: x + y), squareList)

        if (sqTotal) <= 1:
            inCircle += 1
            insideX.append(coordX)
        total+=1
    #result = (math.pow( (4 * inCircle) / total ,(d/2)) * math.pow(1,d)) / (math.gamma((d/2)+1))
    #print("inside the circle=",inCircle)
    #print("approximation=",result)
    return inCircle
    
def main(args):
    time_start = perf_counter()
    n = int(args[1])
    dimension = int(args[2])
    noProcesses = int(args[3])
    result = []
    #process: aynı anda calısacak ıslem sayısı
    print("Part3 Program is running for n=",n," d=",dimension," process=",noProcesses)
    #part2(int(args[1]),int(args[2]))
    #her bir processin kaç işlem hesaplayacağı
    batchSize = int(n/noProcesses)
    list_of_n = [batchSize]*noProcesses 
    # [100,101,100,100,100,100,100,100,100,100] batch size 100 noProcess 10 ise dönecek sonuç
    #print(list_of_n)
    list_of_dimensions = [dimension]*noProcesses
    #[5,5,5,5,5,5,5,5,5] #dimension = 5  noProcess 10 ise dönecek sonuç
    #print(list_of_dimensions)
    with future.ProcessPoolExecutor() as ex:
        result = ex.map(getTotalInCircle,list_of_n,list_of_dimensions) #getTotalInCircle fonksiyonu her bir list_of_n ve list_of_dimensions için çağırılır ve sonuç result listesine tek tek atılır
    #[38,41,55,x...]
    totalInCircle = reduce((lambda x, y: x + y), result)
    #print(list(result))
    approx = (math.pow( (4 * totalInCircle) / n ,(dimension/2)) * math.pow(1,dimension)) / (math.gamma((dimension/2)+1))
    print("inside the circle=",totalInCircle)
    print("approximate=",approx)
    time_stop = perf_counter()
    print("Elapsed time:",  time_stop-time_start, "seconds")


if __name__ == "__main__":
    main(sys.argv)
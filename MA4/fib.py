#!/usr/bin/env python3

from time import perf_counter
import matplotlib.pyplot as plt
from integer import Integer

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

def execute_pure_python(n):
    time_start = perf_counter()
    result = fib_py(n)
    print("fib_py("+str(n)+")=",result)
    time_stop = perf_counter()
    execute_time = time_stop-time_start
    print("fib_py("+str(n)+") Elapsed time:",  execute_time, "seconds")
    return round(execute_time,6)

def execute_cpp(n):
    time_start = perf_counter()
    f=Integer(n)
    print("fib_cpp("+str(n)+")=",f.fib())
    time_stop = perf_counter()
    execute_time = time_stop-time_start
    print("fib_cpp("+str(n)+") Elapsed time:",  execute_time, "seconds")
    return execute_time


def drawPython():
    pyX = []
    pyY = []
    for i in range(30,45):
        pyX.append(i)
        pyY.append(execute_pure_python(i))
    fig, ax = plt.subplots(1)
    ax.set_aspect('auto')
    ax.scatter(pyX, pyY, color='r',edgecolor='y')
    plt.title("pure python fib execution time")
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.savefig('timePy.png')
    plt.show()
    

def drawCpp():
    pyX = []
    pyY = []
    for i in range(30,45):
        pyX.append(i)
        pyY.append(execute_cpp(i))
    fig, ax = plt.subplots(1)
    ax.set_aspect('auto')
    ax.scatter(pyX, pyY, color='r',edgecolor='y')
    plt.title("c++ fib execution time")
    plt.xlabel("n")
    plt.ylabel("seconds")
    plt.savefig('timCpp.png')
    plt.show()

def main():
    drawPython()
    drawCpp()
    execute_cpp(47)

if __name__ == '__main__':
	main()


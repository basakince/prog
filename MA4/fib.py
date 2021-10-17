#!/usr/bin/env python3

from time import perf_counter
from integer import Integer

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))

def execute_pure_python(n):
    time_start = perf_counter()
    print("fib_py("+str(n)+")=",fib_py(n))
    time_stop = perf_counter()
    print("fib_py("+str(n)+") Elapsed time:",  time_stop-time_start, "seconds")

def execute_cpp(n):
    time_start = perf_counter()
    f=Integer(n)
    print("fib_cpp("+str(n)+")=",f.fib())
    time_stop = perf_counter()
    print("fib_cpp("+str(n)+") Elapsed time:",  time_stop-time_start, "seconds")

def main():
    execute_pure_python(30)
    execute_pure_python(45)
    execute_cpp(30)
    execute_cpp(45)
    execute_cpp(47)

if __name__ == '__main__':
	main()
#-----------------------------------------------------------------------
# performance.py
#-----------------------------------------------------------------------

import sys
import time

class Stopwatch:

    # Construct self and start it running.
    def __init__(self):
        # NB: Windows time() function is only second precision :(
        # https://stackoverflow.com/questions/1938048/high-precision-clock-in-python
        self._creationTime = time.perf_counter()  # Creation time

    # Return the elapsed time since creation of self, in seconds.
    def elapsedTime(self):
        return time.perf_counter() - self._creationTime

#-----------------------------------------------------------------------

# Performs unknown computation
def functionA( n ):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            count += 1
    return count

# Performs unknown computation
def functionB( n ):
    count = 1
    while( count < n ):
        count = count * 2
    return count


# Performs unknown computation
def functionC( n ):
    count = 0
    for i in range(n):
        count += 1
    return count

# Performs unknown computation
def functionD( n ):
    count = 0
    for i in range(n):
        s = n
        while( s > 0 ):
            s = s // 2
            count += 1
    return count

# Performs unknown computation
def functionE( n ):
    s = []
    count = 0
    for i in range(n):
        s.insert(0,'a')
        count += 1
    return count

# Performs unknown computation
def functionF( n ):
    if( n == 1 ):
        return 1
    else:
        return n + functionF( n // 2 )

# Performs unknown computation
def functionG( n ):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                count += 1
    return count

# Performs unknown computation
def functionH( n ):
    if( n == 0 ): return 0
    if( n == 1 ): return 1
    return functionH(n-1) + functionH(n-2)


# Performs unknown computation
def functionI( n ):
    count = 0
    for i in range(n):
        for j in range(n):
            functionB(n)
    return count

# Performs unknown computation
def functionJ( n ):
    count = 0
    for i in range(1000000):
        count += 1
    return count

#-----------------------------------------------------------------------

def main():
    # Accept integer n as a command-line argument. Write to standard output
    # a table of doubling ratios for various problems of size n
    # The user will have to kill the program as it is an infinite loop
    if( len(sys.argv) != 3 ):
        print("Usage: python <n> <function from A-J>")
        print("Example: python 100 A")
        return
    
    n            = int(sys.argv[1])
    functionName = sys.argv[2]

    functions = {}
    functions['A'] = functionA
    functions['B'] = functionB
    functions['C'] = functionC
    functions['D'] = functionD
    functions['E'] = functionE
    functions['F'] = functionF
    functions['G'] = functionG
    functions['H'] = functionH
    functions['I'] = functionI
    functions['J'] = functionJ

    # Try some number of trials - hopefully will have converged
    f = functions[functionName]
    print('\nFunction: ' + str(f) )
    print('      n   T(2n)/T(n)    T(2n)      T(n)')
    for t in range(6):
        # Determine time for each function
        watch = Stopwatch()
        f(n)
        timeN = watch.elapsedTime()
        
        
        watch = Stopwatch()
        f(2*n)
        time2N = watch.elapsedTime()

        # Sanity check , windows timers may produce 0 timeN
        if( timeN > 0.0 ):
            ratio = time2N / timeN
            print(f"{n:7d}      {ratio:4.2f}  {time2N:10.6f} {timeN:10.6f}")
        else:
            print("Timer not precise enough, try larger n.")
        n *= 2

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python performance.py 1000 C

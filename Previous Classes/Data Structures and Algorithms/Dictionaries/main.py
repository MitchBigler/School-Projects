# import whatever you need here
import time
import sys
from hashmap import HashMap

# Global vars
function_calls = 0
cache_hits = 0
cache = HashMap()

# Part 1 -- Write weight_on_cacheless() method
def weight_on_cacheless(r, c):
    global function_calls
    function_calls += 1

    # Base case
    if r == 0:
        return 0.0
    # Check if leftside
    if c == 0:
        return weight_on_cacheless(r - 1, c) / 2 + 100
    # Check if rightside
    if c == r:
        return weight_on_cacheless(r - 1, c - 1) / 2 + 100
    # Calculate weight of both
    return (weight_on_cacheless(r - 1, c - 1) + weight_on_cacheless(r - 1, c)) / 2 + 200

# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    global function_calls, cache_hits
    function_calls += 1

    # Cache check
    try:
        value = cache.get((r,c))
        cache_hits += 1
        return value
    except:
        # Base case
        if r == 0:
            weight = 0.0
        # Check if leftside
        elif c == 0:
            weight = weight_on_with_caching(r - 1, c) / 2 + 100
        # Check if rightside
        elif c == r:
            weight = weight_on_with_caching(r - 1, c - 1) / 2 + 100
        # Calculate weight of both
        else:
            weight = (weight_on_with_caching(r - 1, c - 1) + weight_on_with_caching(r - 1, c)) / 2 + 200

        # Add to cache
        cache.set((r,c), weight)
        return weight


def main():
    global function_calls

    # Cacheless
    print("Cacheless:")
    function_calls = 0
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("cacheless.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("\nElapsed time: " + str(elapsed) + " seconds.")
    print(f"Number of function calls: {function_calls}")

    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.write(f"Number of function calls: {function_calls}\n")

    f.close()
    
    # # Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    # With Caching
    print("With Caching:")
    function_calls = 0
    
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])

    f = open("with_caching.txt","w")

    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_with_caching(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start

    print("\nElapsed time: " + str(elapsed) + " seconds.")
    print(f"Number of function calls: {function_calls}")
    print(f"Number of cache hits: {cache_hits}")

    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    f.write(f"Number of function calls: {function_calls}\n")
    f.write(f"Number of cache hits: {cache_hits}\n")

    f.close()

if __name__=="__main__":
    main()


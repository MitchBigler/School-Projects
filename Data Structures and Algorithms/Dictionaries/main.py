# import whatever you need here
import time
import sys

function_calls = 0

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
    # Recursively calculate weight on the back of the person
    return (weight_on_cacheless(r - 1, c - 1) + weight_on_cacheless(r - 1, c)) / 2 + 200

# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    pass

def main():
    global function_calls

    # weight_on_cacheless tests
    # print(f'(1,0): {weight_on_cacheless(1,0)}')
    # print(f'(2,0): {weight_on_cacheless(2,0)}')
    # print(f'(2,1): {weight_on_cacheless(2,1)}')
    # print(f'(3,0): {weight_on_cacheless(3,0)}')
    # print(f'(3,1): {weight_on_cacheless(3,1)}')

    # Part 2 -- Use weight_on_cacheless() method
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
    # pass

if __name__=="__main__":
    main()


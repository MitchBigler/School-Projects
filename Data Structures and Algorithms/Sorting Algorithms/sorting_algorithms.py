def is_sorted(lyst):

    if not isinstance(lyst, list):
        raise TypeError
    
    for i in lyst:
        if not isinstance(i, int):
            raise TypeError
        
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i - 1]:
            return False

    return True

############## SELECTION SORT ##############
def selection_sort(lyst):
    # Initialize tracking vars
    comps = 0
    swaps = 0

    # For each element but the last, find and sort the smallest
    for i in range(0, len(lyst) - 2):
        # Assign the smallest value to min_index. Start with first
        min_index = i

        # Search through each element and compare with current min
        for j in range(i + 1, len(lyst)):
            comps += 1
            if lyst[j] < lyst[min_index]:
                min_index = j

        # Swap the min with the current element
        temp = lyst[i]
        lyst[i] = lyst[min_index]
        lyst[min_index] = temp
        swaps += 1
        #print(lyst)

    return lyst, comps, swaps


############## INSERTION SORT ##############
def insertion_sort(lyst):
    # Initialize tracking vars
    comps = 0
    swaps = 0

    # For each element starting at one compare against previous elements
    for i in range(1, len(lyst)):
            # Compare against every element that is less than current
            for j in range(i, 0, -1):
                comps += 1
                # Swap elements if current element is less
                if lyst[j-1] > lyst[j]:
                    swaps += 1

                    temp = lyst[j-1]
                    lyst[j-1] = lyst[j]
                    lyst[j] = temp
                else:
                    break

    return lyst, comps, swaps


############## MERGE SORT ##############
def mergesort(lyst):
    # Helper function to implement with start and end parameters
    def mergesort_helper(lyst, start, end):
        # Base case: only one element
        if end == start:
            return [lyst[start]], 0, 0

        mid = (start + end) // 2

        # Recursively sort left and right
        left_s, left_comps, left_swaps = mergesort_helper(lyst, start, mid)
        right_s, right_comps, right_swaps = mergesort_helper(lyst, mid + 1, end)

        # Merge the sorted halves
        sorted_lyst, comps, swaps = merge(left_s, right_s)

        return sorted_lyst, (left_comps + right_comps + comps), (left_swaps + right_swaps + swaps)

    # Call the helper function with full list range
    return mergesort_helper(lyst, 0, len(lyst) - 1)

def merge(left, right):
    i = 0
    j = 0
    temp = []
    comps = 0
    swaps = 0

    # Compare elements from left and right and merge them in sorted order
    while i < len(left) and j < len(right):
        comps += 1
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    # Add remaining elements from left
    while i < len(left):
        temp.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < len(right):
        temp.append(right[j])
        j += 1

    return temp, comps, 0


############## QUICK SORT ##############
def quicksort(lyst):
    # Helper function to implement with start and end parameters
    def quicksort_helper(lyst, start, end):
        # Base case: return if sublist has 1 element or is empty
        if start >= end:
            return lyst, 0, 0
        
        # Partition list and get pivot index
        pivot_index, comps, swaps = partition(lyst, start, end)

        # Recursively sort the left and right sublists
        l_sub, l_comps, l_swaps = quicksort_helper(lyst, start, pivot_index)
        r_sub, r_comps, r_swaps = quicksort_helper(lyst, pivot_index+1, end)

        return lyst, comps + l_comps + r_comps, swaps + l_swaps + r_swaps
    
    # Call the helper function with full list range
    return quicksort_helper(lyst, 0, len(lyst) - 1)


def partition(lyst, left, right):
    # Chose pivot as mid point
    pivot_index = int((left + right)/2)
    pivot = lyst[pivot_index]

    # Initialize tracking vars
    finished = False
    comps, swaps = 0,0

    while not finished:
        # Move left index to right until element greater than pivot
        while lyst[left] < pivot:
            comps += 1
            left += 1
        comps += 1

        # Move right index to right until element less than pivot
        while lyst[right] > pivot:
            comps += 1
            right -= 1
        comps += 1

        # Swap elements if left is less than right
        if left < right:
            comps += 1

            if lyst[left] > lyst[right]:
                #print(f'Swap {lyst[left]} with {lyst[right]}')
                temp = lyst[left]
                lyst[left] = lyst[right]
                lyst[right] = temp

                swaps += 1
                left += 1
                right -= 1
        else:
            comps += 1
            finished = True

    return right, comps, swaps




############## MAIN ##############
def main():
    print("------------------------------")
    test_nums = [1,3,5,7,9,3,2]
    print(test_nums)
    print(quicksort(test_nums))
    print("------------------------------")

if __name__=="__main__":
    main()
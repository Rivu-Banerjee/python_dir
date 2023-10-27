# Problem Statement 
# Implement Bubble Sort for Python

------------------------------------
------------------------------------

# Solution

def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
 
elements = [39, 12, 18, 85, 72, 10, 2, 18]
 
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)


# Output

Unsorted list is,
[39, 12, 18, 85, 72, 10, 2, 18]
Sorted Array is, 
[2, 10, 12, 18, 18, 39, 72, 85]

# Complexity

Time Complexity: O(n2).
Auxiliary Space: O(1).

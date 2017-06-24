import time

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <=pivot]
        greater = [i for i in arr[1:] if i >=pivot]

        return quicksort(lesser) + [pivot] + quicksort(greater)

start_time = time.time()
print quicksort([5,3,6,2,10])
print("Total Time taken %s seconds" % (time.time() - start_time))
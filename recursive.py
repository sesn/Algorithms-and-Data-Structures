import time
def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        total = arr[0] + sum(arr[1:])
    return total

def normal_sum(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total
        
    
number_list = [2,4,5,6,7,12,3,4,4,2,3,5,2,2,5,5,5,5,5,5,5]
start_time = time.time()
print recursive_sum(number_list);
print("Total Time taken %s seconds" % (time.time() - start_time))
print ""
print ""
start_time = time.time()
print("The normal total function is %s" % normal_sum(number_list))
print("Total Time taken %s seconds" % (time.time() - start_time))


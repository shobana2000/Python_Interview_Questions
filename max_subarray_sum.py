sumarray=[1, 2, 3, -2, 5]

def max_subarray_sum(arr):
    aray=arr[0]
    curr_ar=arr[0]
    for i in range(1,len(arr)):

        curr_ar=max(arr[i],curr_ar+arr[i])

        aray=max(aray,curr_ar)

    return aray

val=max_subarray_sum(sumarray)
# print(val)
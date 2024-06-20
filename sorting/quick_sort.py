def quick_sort(arr,low,high): 

    if len(arr) <= 1 : 
        return arr 

    p_index = partition(arr)
    quick_sort(arr,low,p_index-1) 
    quick_sort(arr,low,p_index+1) 
    

def partition(arr, low , high): 

    pivot = arr[low] 
    i = low 
    j = high 

    while i < j : 

        while arr[i] <= pivot : 
            i += 1 
        
        while arr[j] > pivot : 
            j -= 1
        
        arr[i] ,arr[j] = arr[j] ,arr[i]

    return j 


array = [10 , 20 , 30, 50, 90, 9] 
sort_array = quick_sort(array) 
print(sort_array)


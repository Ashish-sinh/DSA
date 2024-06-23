def quick_sort(arr,low,high): 

    if low < high : 
        p_index = partition(arr,low,high)
        quick_sort(arr,low,p_index-1) 
        quick_sort(arr,p_index+1,high) 
    
    return arr

def partition(arr, low , high): 

    pivot = arr[low]
    i = low 
    j = high 

    while i < j : 

        while arr[i] <= pivot and i < high :  # step 1 
            i += 1 

        while arr[j] > pivot and j > low :  # step 2 
            j -= 1
        # May be possible after this both steps i and j have crossed  if crossed then direct this controll go to steps 4 


        # so now Only swap if i and j have not crossed each other
        if i < j : # steps 3 
            arr[i] ,arr[j] = arr[j] ,arr[i]
    
    # steps 4 
    # swap if low and j is crossed mean all left side are smaller and right side are higher 
    arr[low],arr[j] = arr[j] ,arr[low]
        
    return j 

array = [10 , 20 , 30, 50, 90, 9] 
sort_array = quick_sort(array,0,len(array)-1) 
print(sort_array)
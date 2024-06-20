def merge_sort(arr) : 
    
    if len(arr) == 0 or len(arr) == 1: 
        return arr 
    
    mid = len(arr) // 2 
    left = arr[:mid]  # mid is exclude 
    right = arr[mid:] 

    # now we have 2 split and we wanted to sort that 2 split so for sorting both the split again we do merget sort on that 

    left_sorted_split = merge_sort(left) 
    right_sorted_split= merge_sort(right) 

    merged_sorted_array = merge(left_sorted_split,right_sorted_split) 

    return merged_sorted_array

def merge(left_array, right_array) : # consider this both array is sorted array 

    i, j = 0, 0 
    arr = [] 

    while i < len(left_array) and j < len(right_array) : 

        if left_array[i]<= right_array[j] :  # if eliment of left array is smaller then append it 
            arr.append(left_array[i]) 
            i += 1 

        else : 
            arr.append(right_array[j])  # otherwise the eliment of right array is samller then append that eliment into arr
            j += 1 
        
    while i < len(left_array) : 
        arr.append(left_array[i]) 
        i += 1 
    
    while j < len(right_array) : 
        arr.append(right_array[j]) 
        j += 1 
    
    return arr 



array = [10 , 20 , 80 , 90 , 110 , 30 , 50 ] 
sorted_array = merge_sort(arr=array) 
print(sorted_array) 


 
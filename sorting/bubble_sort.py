def bobble_sort(arr) : 

    n = len(arr) 

    for i in range(n-2,-1,-1) : 

        for j in range(0 , i+1) : 
            
            if arr[j] > arr[j+1] : 

                arr[j] , arr[j+1] = arr[j+1] , arr[j] 
    return arr 

array = [90 , 20 , 50 , 60 , 20 , 70 ] 
sorted_array = bobble_sort(array) 
print(sorted_array) 

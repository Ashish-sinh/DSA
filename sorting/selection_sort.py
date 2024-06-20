def selection_sort(array) : 

    n = len(array) 

    for i in range(n) : 
        
        min_index = i
        
        for j in range(i+1 ,n) : 

            if array[j] < array[min_index]:
                min_index = j 
        
        a[i] , a[min_index] = a[min_index] , a[i] 
    
    return array

a = [10 , 20 , 60 , 50 , 30 , 90 ]
sorted_a = selection_sort(a) 
print(sorted_a) 


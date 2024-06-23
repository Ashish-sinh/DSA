# https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957


def isSorted(n: int, a) -> int:

    for i in range(n-1) : 

        if a[i] <= a[i+1] : 
            continue 
        else : 
            return 0 
            break 
         
    
    return 1 

x = [1,2,3,4,5,6,7]  
print(isSorted(7,x))  # print 1 if array is sorted in increasing order and 0 if array is sorted in descreasing order.. 
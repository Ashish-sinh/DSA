# palindrome with reducing the size of string :

def palindrome(string) : 

    if len(string) == 0 or len(string) == 1 : 
        return True 
    
    if string[0] == string[-1] : 
        return palindrome(string[1:-1]) 

    return False

result = palindrome('ashishsihsa')
print(result) 


def palindrome2(string:str ,n:int) : 

    if n >= len(string)//2 : 
        return True 
    
    if string[n] == string[~n] : 
        return palindrome2(string , n+1) 
    
    return False 

res = palindrome2('123321',0) 
print(res) 



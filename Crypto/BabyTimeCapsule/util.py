def fifth_root(n):

    if n == 0 or n == 1:

        return n
    
    else:
        
        low = 0
        high = n
        
        while True:
            mid = (low + high) // 2
            mid5 = mid**5
    
            if mid5 == n: 
                
                return mid 
            
            if mid5 < n: 
                
                low = mid+1
            
            elif mid5 > n: 

                high = mid-1
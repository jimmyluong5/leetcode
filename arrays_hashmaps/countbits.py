
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    
    i = 1 #initialize the iterating pointer.
    one_count = 0
    res = [] #start with an empty list instead of [0] * n , because most of it will be empty junk of 0s.
    #we need to place the numbers to the back of the array because they go to the top of the array.
    one = [] #this array will consist of the number of ones in the number, then at the end just join the arrays together.
    
    n_len = n.bit_length() #determine the bit length which helps with the placement of indices.
    
    while n > 0:
        
        #if the modulate is one, we can keep track of that and later place it in the resulting array.
        if (n%2 == 1):
            one_count +=1
            res.append(n_len-i+1) #we append the index to the end of the resulting array instead of the start.
            
            
        
        #calculate the next n    
        n = n//2
        #move the pointer
        i+=1
    one.append(one_count)
    
    one = one+res[::-1] 
    return one  
    
    
        
    

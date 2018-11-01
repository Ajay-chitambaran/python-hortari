import collections 
 
def CountFrequency(arr): 
    return collections.Counter(arr)   
  
# Driver function 
if __name__ == "__main__": 
  
    arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5] 
    freq = CountFrequency(arr) 
  
    # iterate dictionary named as freq to print 
    # count of each element 
    for key, value in freq.iteritems(): 
        print key, " -> ", value 

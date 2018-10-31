def numpat():   
    num =values[0]
	print("enter values:\n")
	data=input()
	values=data.split(" ")
    # outer loop to handle number of rows 
    for i in range(0,len(values)): 
      
        # re assigning num 
        num =values[0]
      
        # inner loop to handle number of columns 
            # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
                # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num =num+1
      
        # ending line after each row 
        print("\r") 
  
# Driver code 
n = 5
numpat(n) 

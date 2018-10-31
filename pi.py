def insert():
	print("enter values:\n")
	data=input()
	values=data.split(" ")
	for i in range(0,len(values)):
		
		for j in range(0,i+1):
			print(values[i],end=" ")
			
			#values[i]=values[i+1]
		print("\n")
	#count=len(array)
	#print(count)		
insert()		

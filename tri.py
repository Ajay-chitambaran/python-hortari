array=[]
for i in range(0,3):
	print("Enter values\n")
	data=int(input())
	print("done!!\n")
	array.append(data)
sum=array[0]+array[1]+array[2]
if(sum==180):print(" Its a triangle!!\n")
else:print(" Not a triangle!!\n")

array=[]
print("Enter length:\n")
leng=input()
leng=int(leng)
for i in range(0,leng):
	print("-------------Entering data-----------")
	val=input(int())
	array.append(val)
print(len(array))
def check():
	count=0
	for j in range(0,len(array)):
		for k in range(j,len(array)):
			if(array[j]==array[k]):
				count=count+1
				print("No of duplicates=",count)
check()
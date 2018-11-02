array=[]
print("Enter length:\n")
leng=input()
leng=int(leng)
for i in range(0,leng):
	print("-------------Entering data-----------")
	val=input(int())
	array.append(val)
#print(len(array))
def check():
	element=0
	count=0
	for j in range(0,len(array)):
		tempelement=array[j]
		tempcount=0
		for k in range(0,len(array)):
			if(tempelement==array[k]):
				tempcount=tempcount+1				
		if(tempcount>>count):
			element=tempelement
			count=tempcount
	print("most frequent element is",element)
check()

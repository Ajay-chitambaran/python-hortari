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
	count=0
	for j in range(0,len(array)):
		head=array[j]
		for k in range(0,len(array)):
			if(head==array[k]):
				count=count+1				
				dict={'val':head,'rep':count}
	print(dict.values())
check()

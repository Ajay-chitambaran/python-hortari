array=[]
print("Enter length: \n")
len=input()
len=int(len)
print("Length entered successfully!\n")
def insertion(length):
	print("--------------Insert_values-------------------")
	for i in range(0,length):
		data=input(int())
		array.append(data)
		print("inserted successfully!\n")
insertion(length=len)
def find():
	count=0
	for i in range(0,len):
		for j in range(i+1,len):
			if(array[i]==array[j]):
				count=count+1
	print (array)
	print(count,"sets are present in this array")
find()
	

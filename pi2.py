array=[]
data=input(int())#input is taken
array=data.split(" ")#input is converted to strings
#print(array)
#print(len(values))
for i in range(0,len(array)+1):
	#print(array[:i])
	print(" ".join(array[:i]))#strings are sliced
print("\n")
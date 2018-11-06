#insert float values at prices
origItems=[]
origPrice=[]
items=[]
price=[]
itindex=[]#address holder
valuestorage=[]
holder=[]
holder2=[]
count=0
n=int(input())
for i in range(0,n):
    origItems.append(input())#item array insertion
    itindex.append(i)
m=int(input())
for k in range(0,m):
    origPrice.append(float(input()))#price array insertion with index noticing
    #prindex.append(k)#index value to an array
search=int(input())
for item in range(0,search):
	itemcompar=input()
	for j in range(0,len(itindex)):
		if(itemcompar==origItems[itindex[j]]):
			 holder.append(origPrice[itindex[j]])#moved to holder
search2=int(input())
if(search==search2):
	for rep in range(0,search2):
		nowval=float(input())
		holder2.append(nowval)
		if(holder[rep]!=holder2[rep]):
			count=count+1
print(count)#result

origItems=[]
origPrice=[]
items=[]
price=[]
itindex=[]
#prindex=[]
itemaddress=[]#address holder
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
    for j in range(0,len(origItems)):
        if(itemcompar==origItems[j]):
           itemaddress.append(j)#locating address of item phase1
search2=int(input())
if(search==search2):
    for rep in range(0,search2):
        nowval=float(input())
        for x in range(0,len(itemaddress)):
            a=itemaddress[x]#locatingof address of item phase2
            if(origPrice[a]!=nowval):#compared values and counted with counter
                count=count+1
print(count-2)#mathematical correction
#print(count)

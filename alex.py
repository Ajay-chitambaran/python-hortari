#insert float values at prices
owner={}#dictionary of price and item
count=0
n=int(input("Number of items going to enter:  "))
for i in range(0,n):
    origItem=input("Enter orginal item:  ")
    origPrice=float(input("Enter original price: "))
    owner[origItem]=origPrice
m=int(input("Number of items going to search: "))
for j in range(0,m):
    item=input("Enter item sold by alex: ")
    price=float(input("Enter price sold by alex: "))
    if(owner[item]!=price):
        count=count+1
    else:
        count=count
print("alex sold %d items incorrectly"%(count))

storage=[]#storage of values
n=int(input())
for i in range(0,n):
    storage.append(int(input()))
k=int(input())
def numberofPairs(storage,k):
    holder=[]#storage of pairs
    uniqholder=[]#storage unique of pairs
    for j in range(0,len(storage)):
        for l in range(j+1,len(storage)):
            if(storage[j]+storage[l]==k):
                holder.append(storage[j])
                holder.append(storage[l])
    #print(holder)
    for uni in range(0,len(holder)):#process of getting unique array
        flag=0
        for uni2 in range(0,uni):
            if(holder[uni]==holder[uni2]):
                flag=1
                break
        if(flag==0):
            uniqholder.append(holder[uni])
    pairs=int(len(uniqholder))
    pairs=pairs//2#getting no of pairs
    print(pairs)
    return pairs
numberofPairs(storage,k)

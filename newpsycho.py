scores=[]
lowers=[]
uppers=[]
def test():
    n=input()
    n=int(n)#no of elements
    for j in range(0,n):
        b=input()
        b=int(b)#scores input
        scores.append(b)
        print(scores)
    c=int(input())#no of lowerlimits
    for i in range(0,c):
        d=int(input())#values for lowerlimits
        lowers.append(d)
        print(lowers)
    e=int(input())#no of upperlimits
    for k in range(0,e):
        f=int(input())#values for upprlimits
        uppers.append(f)
        highlimiter=(max(uppers))#setting highest position
        lowlimiter=(min(lowers))#setting lowest position
    count=0
    for i in range(0,len(scores)):
        if(lowlimiter<=scores[i])and(highlimiter>=scores[i]):#condition for passing
            count=count+1
        else:
            pass
    #print(count)
    return count
test()

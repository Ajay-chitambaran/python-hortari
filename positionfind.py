#a=[4,1]
#b=[1,2,3,4,5]
#pos=[]
#jj=0
#for i in range(0,len(b)):
#    for k in range(0,len(a)):
#        x=a[k-1]
#        y=b[i-1]
#        while int(x)==int(y):
#            jj+=1
#        if(a>>2):
#            break
#        print(jj)

n = 100

s = 0
counter = 1
while counter <= n:
    s = s + counter
    counter += 1

print("Sum of 1 until %d: %d" % (n,s))

ascii="abcdefghijklmnopqrstuvwxyz"#{example output for further}
stringstorage=[]
result=[]#returnstring
def ispangram(stringdata):
    stringdata=stringdata.lower()#correcting case issues
    collector=''.join(sorted(stringdata))#sorting
    collector=collector.replace(" ","")#removing spaces
    final=''.join(set(collector))#removing repetition
    final=''.join(sorted(final))
    if(ascii==final):
        result.append("1")#true case pushing to result
    else:
        result.append("0")#false case pushing to result
    giver=(''.join(result))
    return giver
a=int(input())#first line
for rep1 in range(0,a):
    stringdata=input()
    ispangram(stringdata)

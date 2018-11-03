#Q-1012
holder=[]
def holefinder():
    giveno=input()
    converter=(" ".join(giveno))#given spaces for future splitting
    splitter=converter.split(" ")#splitting is done and stored as array
    count=0
    for i in range(0,len(splitter)):
        if(int(splitter[i-1])==8):#i-1 is given to begin with 0
            count=count+2
        elif(int(splitter[0])==0):
            count=count+1
        elif(int(splitter[i-1])==4):
            count=count+1
        elif(int(splitter[i-1])==6):
            count=count+1
        elif(int(splitter[i-1])==9):
            count=count+1
        elif(int(splitter[i-1])==1):
            count=count
        elif(int(splitter[i-1])==2):
            count=count
        elif(int(splitter[i-1])==3):
            count=count
        elif(int(splitter[i-1])==5):
            count=count
        elif(int(splitter[i-1])==7):
                count=count
    print(count)
    return(count)
holefinder()

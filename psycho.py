scores=[]
lowers=[]
uppers=[]
final=[]
positions=[0]
print("working")
def test():
	n=input()
	n=int(n)#no of elements
	for j in range(0,n):
		b=input()
		b=int(b)#scores
		scores.append(b)
	#scores.sort()
	print(scores)
	c=int(input())#no of lowerlimits
	for i in range(0,c):
		d=int(input())#values for lowerlimits
		lowers.append(d)
	#lowers.sort()
	print(lowers)
	e=int(input())#no of upperlimits
	for k in range(0,e):
		f=int(input())#values for upprlimits
		uppers.append(f)
	#uppers.sort()
	print(uppers)
	locationxval=min(lowers)
	locationyval=max(uppers)
	print(locationxval)
	print(locationyval)
	print(len(scores))
	print(len(lowers))
	for m in range(0,len(scores)):
		for n in range(0,len(lowers)):
			print(m,n)
			if(scores[m]==locationxval):
				temp1=scores[m]
				place=scores.index(temp1)
				positions.append(place)
		for pos3 in range(0,len(uppers)):
			if(scores[m]==locationyval):
				temp2=scores[m]
				place2=scores.index(temp2)
				positions.append(place2)
	print(positions)
	for l in range(min(positions),max(positions)):
		final.append(scores[l])
	print(final)
	answer=len(final)
	print(answer)
	print("check")
	return answer
test()

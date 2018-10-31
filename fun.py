def find(a,b,c):
	#a=1stside
	#b=2ndside
	#c=3rdside
	count=0
	if(a+b>=c):
		count=count+1
	if(a+c>=b):
		count=count+1
	if(b+c>a):
		count=count+1
	if(count>=2):
		print("its a triangle!!\n")
	else:print("its not a triangle!!\n")
	
find(a=input(),b=input(),c=input())

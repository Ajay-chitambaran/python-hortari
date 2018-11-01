class Split:
	def __init__(self,data):
		self.data=data
		self.broken=data.split(" ")
	def show(self):
		print("before:",self.data,"\nafter:",self.broken)

s=Split(input())
s.show()


class Token:

	def __init__(self, startChar):
		self.value = startChar
		self.type = None

	def display(self):
		#print self.value + " " + self.type
		a = " "
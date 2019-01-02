class Student:
	n = 10
	def __init__(self, name = '', marks = 0):
		self.name = name
		self.marks = marks
	def calculate(self):
		if(self.marks >= 70):
			print('You got A grade')
		elif(self.marks >= 50):
			print('You got B grade')
		elif(self.marks >= 30):
			print('You got C grade')
		else:
			print('You are FAIL')
	class Dob:
		def __init__(self, dd, mm, yy):
			self.dd = dd
			self.mm = mm
			self.yy = yy
		def display(self):
			print('Date: ', self.dd, 'Month: ', self.mm, 'Year: ', self.yy)

n = int(input('How many students? '))
for i in range(n):
	name = str(input('Enter name: '))
	marks = int(input('Enter marks: '))
	month = int(input('Enter month: '))
	date = int(input('Enter Date: '))
	year = int(input('Enter Year: '))
	s = Student(name, marks)
	s.calculate()
	x = s.Dob(date, month, year)
	x.display()

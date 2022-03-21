class Student:
	"""docstring for Student"""
	def __init__(self, first_name,second_name,age,country):
		self.first_name = first_name
		self.second_name = second_name
		self.age = age
		self.country = country
	def full_name(self):
		name= self.first_name + " "+ self.second_name
		return name
	def year_of_birth(self):
		return 2019-self.age	
	def greeting(self):
		return "Hello {}, you were born in {}".format(self.first_name,(2019-self.age))
	    
    def initials(self):
    	initial = self.first_name + self.second_name
    	return initial

	def countries(self):
		return "Hello {}, you have visited {}".format(self.first_name,self.country))	



		
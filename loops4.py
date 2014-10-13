#loops4

class ExamResults:
	def __init__ (self, score = 0):
		self.set_score(score)
		
	def get_score(self):
		return self.__score
	
	def set_score(self, score):
		if (score < 0) or (score > 100):
			raise ValueError
		else:
			self.__score = score
result = ExamResults()
try:
	result.set_score(110)
except ValueError:
	print 'cannot score more than 100%'

result.set_score(79)
print "Exam score: %d%%" % result.get_score()


print "----------------------"

class ExamResults(object):
	def __init__(self, score = 0):
		self.set_score(score)
		
	def get_score(self):
		return self.__score
		
	def set_score(self, score):
		if (score < 0) or (score > 100):
			raise ValueError
		else:
			self.__score = score
	score = property (get_score, set_score)
result = ExamResults()
try:
	result.score = 100
except ValueError:
	print 'Cannot socre more than 100%'
result.score  = 79
print 'Exam score: %d%%' % result.score

def add(x):
	def inc(y):
		return x + y
	return inc
	
	
	
	
	
	
	
	
	
	
	
	
	
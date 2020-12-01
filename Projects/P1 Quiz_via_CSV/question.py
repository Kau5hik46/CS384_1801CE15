class Question():
	def __init__(self, number, q, options, correct, marks, comp = 'n'):
		self.qnum = number

		self.question = str(q)
		if(self.question[-1] != '?'):
			self.question += '?'

		self.options = list(options)
		self.marks = tuple(marks)
		self.obtained_marks = 0
		self.correct = correct

		if comp.upper() == 'Y':
			self.compulsory = "Yes"
			self.comp = True
		else:
			self.compulsory = "No"
			self.comp = False

	def display_question(self):
		print("Question ", self.qnum, ") ", self.question)
		i = 1
		for opt in self.options:
			print("Option ", i, ") ", opt)
		print()
		print("Credits if correct option: ", self.marks[0])
		print("Negative Marking: ", self.marks[1])
		print("Is compulsory: ", self.compulsory)
		self.marking()

	def marking(self):
		self.answer = input("Enter Choice: 1,2,3,4,S : S is to skip question: ")
		try:
			self.answer = int(self.answer)
		except:
			self.answer = str(self.answer)
		acceptable = [1,2,3,4,'S']
		while self.answer not in acceptable:
			self.answer = input("Enter Choice: 1,2,3,4,S : S is to skip question: ")

		if(self.answer == self.correct):
			self.obtained_marks = self.marks[0]
		elif self.answer == 'S' and not self.comp :
			self.obtained_marks = 0
		else:
			self.obtained_marks = self.marks[1]

		return self.obtained_marks

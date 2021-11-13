import random as rand

"""
This is the lottery bot class that will guess powerball numbers
an perform various other data analysis as updated.
@Author: Nolan Jordan
"""

class lotbot:
# constructor #
	def __init__(self, sample = [0,0,0,0,0], spower = 0):
		self.sample = []
		self.spower = spower
		self.value = [0,0,0,0,0]
		self.power = 0

# class methods #

	# randomising algorithim that follows typical rules of powerball #
	def randomGuess(self):
		temp = self.value
		self.check()
		for x in range(len(temp)):
			temp[x] = rand.randint(1,69)
		#sort list from least to greatest#
		temp.sort()
		self.power = rand.randint(1, 26)
		self.value = temp

	# show the screan results #
	def show(self):
		print("Numbers: " +str(self.value))
		print("Powerball: " + str(self.power))

	# show the loaded sample #
	def showSample(self):
		print("Sample Numbers: " +str(self.sample))
		print("Sample Powerball: " + str(self.spower))

	# send data to anouther source/script #
	def send(self):
		output = self.value
		output.append(self.power)
		return output

	# sometimes the lotbot will append to much data #
	# this method will delete the extra data #
	# Fix: find reason for double append #
	def check(self):
		temp = self.value
		size = len(temp)
		while size > 5:
			temp.pop()
			size = size - 1
		self.value = temp
			
	
    
        

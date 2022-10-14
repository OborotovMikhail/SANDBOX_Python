import random

numbersRange = 10 # Range of numbers to generate (set as a parameter)
numbersNum = 10 # A number of numbers to generate (set as a parameter)

####################### Some functions #######################

# Fuction that generates numbers into a file
def generateToFile(filename, numRange, numNum):
	file = open(filename, 'w') # Opening the file
	for i in range((numNum - 1)):
		file.write(str(random.randint(-numRange, numRange)))
		file.write(' ')
	file.write(str(random.randint(-numRange, numRange)))
	return

# Fuction that reads data from a file
def readFromFile(filename):
	data = [] # Creating an array
	file = open(filename, 'r') # Opening the file
	for number in file.readline().split(' '):
		# Reading numbers from the file to the array
		data.append(int(number))
	return data

####################### Custom array operation functions #######################

# Function that finds the min number in the array
def _min(array):
	result = array[0]
	for number in array:
		if number < result:
			result = number
	return result

# Function that finds the max number in the array
def _max(array):
	result = array[0]
	for number in array:
		if number > result:
			result = number
	return result

# Function that finds the sum of all the numbers of the array
def _sum(array):
	result = 0
	for number in array:
		result += number
	return result

# Function that finds the product of all the numbers of the array
def _mult(array):
	result = 1
	for number in array:
		result *= number
	return result

####################### Main #######################



####################### Main #######################

generateToFile('data.txt', numbersRange, numbersNum)
data = readFromFile('data.txt')

print('min = ', _min(data))
print('max = ', _max(data))
print('sum = ', _sum(data))
print('mult =', _mult(data))
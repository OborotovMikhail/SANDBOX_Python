import sys
import matplotlib.pyplot as plt
import random
import time

####################### Parameters #######################

numbersRange = 10 # Range of numbers to generate (set as a parameter)
numbersNum = 10000 # A number of numbers to generate (set as a parameter)

numNumLimit = 10000 # Limit of numbers in the array for elapsed time testing (set as a parameter)
numNumSteps = 100 # Number of steps for elapsed time testing (set as a parameter)

numFunc = 4 # Number of custom functions (set as a parameter)

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

# Function to visualize calculation progress
# Source: https://stackoverflow.com/questions/3160699/python-progress-bar
def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        out.write("%s[%s%s] %i/%i\r" % (prefix, u"#"*x, "."*(size-x), j, count))
        out.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    out.write("\n")
    out.flush()

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


####################### Measuring times #######################

timeArray = [[] for i in range(4)] # Array of elapsed times

stepLen = numNumLimit // numNumSteps # One step length

# Calculating times for _min
for step in progressbar([i for i in range(numNumSteps)], "Computing _min:  ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _min(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[0].append(float((clockEnd - clockStart)) / (10. ** 6))

# Calculating times for _max
for step in progressbar([i for i in range(numNumSteps)], "Computing _max:  ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _max(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[1].append(float((clockEnd - clockStart)) / (10. ** 6))

# Calculating times for _sum
for step in progressbar([i for i in range(numNumSteps)], "Computing _sum:  ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _sum(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[2].append(float((clockEnd - clockStart)) / (10. ** 6))

# Calculating times for _mult
for step in progressbar([i for i in range(numNumSteps)], "Computing _mult: ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _mult(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[3].append(float((clockEnd - clockStart)) / (10. ** 6))


####################### Plotting times #######################

# Creating a figure for plotting times (separately)
figTimes, axTimes = plt.subplots(2, 2)
figTimes.canvas.manager.set_window_title('Time plots')

howManyNums = [i * stepLen for i in range(numNumSteps)] # Array for numbers axis

# Plotting
axTimes[0, 0].plot(howManyNums, timeArray[0], label='Times for _min()', color='tab:blue') # Plot for _min
axTimes[0, 1].plot(howManyNums, timeArray[1], label='Times for _max()', color='tab:orange') # Plot for _max
axTimes[1, 0].plot(howManyNums, timeArray[2], label='Times for _sum()', color='tab:green') # Plot for _sum
axTimes[1, 1].plot(howManyNums, timeArray[3], label='Times for _mult()', color='tab:red') # Plot for _mult

# Setting plot parameters
for i in range(numFunc):
	axTimes[i // 2, i % 2].set_xlabel('Amount of numbers')
	axTimes[i // 2, i % 2].set_ylabel('Time, ms')
	axTimes[i // 2, i % 2].legend(loc='upper left')
	axTimes[i // 2, i % 2].grid(linestyle='--')


# Creating a figure for plotting times (all together)
figTimesAll, axTimesAll = plt.subplots(1, 1)
figTimesAll.canvas.manager.set_window_title('Time plots (all together)')

# Plotting
axTimesAll.plot(howManyNums, timeArray[0],  label='Times for _min()', color='tab:blue')
axTimesAll.plot(howManyNums, timeArray[1],  label='Times for _max()', color='tab:orange')
axTimesAll.plot(howManyNums, timeArray[2],  label='Times for _sum()', color='tab:green')
axTimesAll.plot(howManyNums, timeArray[3],  label='Times for _mult()', color='tab:red')

# Setting plot parameters
axTimesAll.set_xlabel('Amount of numbers')
axTimesAll.set_ylabel('Time, ms')
axTimesAll.legend(loc='best')
axTimesAll.grid(linestyle='--')


# Showing all figures
plt.show()


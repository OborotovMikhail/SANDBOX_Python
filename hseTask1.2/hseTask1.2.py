import sys
import matplotlib.pyplot as plt
import random
import time

numbersRange = 10 # Range of numbers to generate (set as a parameter)
numbersNum = 10000 # A number of numbers to generate (set as a parameter)

numNumLimit = 10000 # Limit of numbers in the array for elapsed time testing (set as a parameter)
numNumSteps = 1000 # Number of steps for elapsed time testing (set as a parameter)

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

####################### Main #######################



####################### Main #######################


####################### Measuring time #######################

timeArray = [[], [], [], []] # Array of elapsed times

stepLen = numNumLimit // numNumSteps # One step length

# Calculating times for _min
for step in progressbar([i for i in range(numNumSteps)], "Computing _min: ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _min(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[0].append((clockEnd - clockStart) // 1000)

# Calculating times for _max
for step in progressbar([i for i in range(numNumSteps)], "Computing _max: ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _max(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[1].append((clockEnd - clockStart) // 1000)

# Calculating times for _sum
for step in progressbar([i for i in range(numNumSteps)], "Computing _sum: ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _sum(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[2].append((clockEnd - clockStart) // 1000)

# Calculating times for _mult
for step in progressbar([i for i in range(numNumSteps)], "Computing _mult: ", 40):
	generateToFile('data.txt', numbersRange, step * stepLen)
	data = readFromFile('data.txt')
	clockStart = time.time_ns() # Time start
	result = _mult(data) # Calculating
	clockEnd = time.time_ns() # Time stop
	timeArray[3].append((clockEnd - clockStart) // 1000)


# Plotting 
figTimes, axTimes = plt.subplots(2, 2)
figTimes.canvas.manager.set_window_title('Time plots')

howManyNums = [i * stepLen for i in range(numNumSteps)]

# Plot for _min
axTimes[0, 0].plot(howManyNums, timeArray[0])
axTimes[0, 0].set_title('Time plot for _min()')
axTimes[0, 0].set_xlabel('Amount of numbers')
axTimes[0, 0].set_ylabel('Time, ms')
plt.grid(linestyle='--')

# Plot for _max
axTimes[0, 1].plot(howManyNums, timeArray[1])
axTimes[0, 1].set_title('Time plot for _max()')
axTimes[0, 1].set_xlabel('Amount of numbers')
axTimes[0, 1].set_ylabel('Time, ms')
plt.grid(linestyle='--')

# Plot for _sum
axTimes[1, 0].plot(howManyNums, timeArray[2])
axTimes[1, 0].set_title('Time plot for _sum()')
axTimes[1, 0].set_xlabel('Amount of numbers')
axTimes[1, 0].set_ylabel('Time, ms')
plt.grid(linestyle='--')

# Plot for _mult
axTimes[1, 1].plot(howManyNums, timeArray[3])
axTimes[1, 1].set_title('Time plot for _mult()')
axTimes[1, 1].set_xlabel('Amount of numbers')
axTimes[1, 1].set_ylabel('Time, ms')
plt.grid(linestyle='--')

# Plotting all together
figTimesAll, axTimesAll = plt.subplots(1, 1)
figTimesAll.canvas.manager.set_window_title('Time plots (all together)')
axTimesAll.set_title('Time plots (all together)')
axTimesAll.plot(howManyNums, timeArray[0],  label='_min()')
axTimesAll.plot(howManyNums, timeArray[1],  label='_max()')
axTimesAll.plot(howManyNums, timeArray[2],  label='_sum()')
axTimesAll.plot(howManyNums, timeArray[3],  label='_mult()')

# Showing all figures
plt.show()


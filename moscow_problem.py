data = input('Enter data: ')


counter = 0
side = 'L'
for i in range(1, len(data)):
	if (data[i - 1] == 'B'):
		print(str(i) + ' crossed B')
		counter += 1
	#elif (((side == data[i - 1]) and (side == data[i])) or ((side == data[i - 1]) and (data[i] == 'B'))):
	elif (((side == data[i - 1]) and (side == data[i]))):
		if (side == 'L'):
			side = 'R'
		elif (side == 'R'):
			side = 'L'
		print(str(i) + ' changed to ' + side)
		counter += 1
	elif(side == data[i - 1]):
		print(str(i) + ' crossed on side ' + side)
		counter += 1
if ((side == 'R') and ((data[len(data) - 1] == 'B') or (data[len(data) - 1] == 'R'))):
	counter += 1
if ((side == 'L') and ((data[len(data) - 1] == 'B') or (data[len(data) - 1] == 'L'))):
	counter += 1
print(counter)
# Test data

# RRLRBRRLLR
# 4

# RRLRBRRLLRBRBRB
# 8

# LLBLRRBRL
# 5
#Header files
import time
import random
import numpy as np
import matplotlib.pyplot as plt


#Function for BinarySearch
def binSearch(referenceArray, searchElement):
	length=len(referenceArray)
	lowerBound = 0
	upperBound = length-1

	while lowerBound <= upperBound:
		middle = floor((lowerBound+upperBound)/2)
		if referenceArray[middle] < searchElement:
			lowerBound = middle+1
		elif referenceArray[middle] > searchElement:
			upperBound = middle-1
		else:
			return middle
	return -1


##Driver Code

#Base declaration
sizeList = []
size = 5
timeList = []

#Loop to find 5 points for Graph plotting
for i in range(12):
	
	#Size in the exponential order of 3
	size = size*3
	
	#Random array generation 
	randomList = random.sample(range(0,10000000), size)
	randomList.sort()
	sizeList.append(size)
	randomArray = np.array(randomList)
	
	#Start of Time evaluation
	start = time.time()
	
	#To be searched
	value = 101

	#Return value form function call
	index = binSearch(randomArray, value)
	#If found
	if index >= 0:
		print("{} is at index {}".format(randomArray[index], index))
	#if not found
	else:
		print("Not found")

	#End of Time evaluation
	stop = time.time()
	timeTaken = (stop-start)
	timeList.append(timeTaken)

#	print(i)
#	print(sizeList)
#	print(randomArray)
#	print(timeTaken)

#Graph - Size of Array vs Time Taken to perform Binary Search
plt.figure(figsize=(50,50))
plt.plot(sizeList, timeList, label="Plot")
plt.plot()
plt.title("Plot")
plt.ylabel("Time Taken")
plt.xlabel("Number of Elements")
plt.grid(axis="both")
plt.show()
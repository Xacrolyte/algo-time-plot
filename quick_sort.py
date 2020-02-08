#Header files
import time
import random
import numpy as np
import matplotlib.pyplot as plt


#Function for Quick Sort
def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  
        # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  
    # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

##Driver Code

#Base declaration
sizeList = []
size = 5
timeList = []

#Loop to find 5 points for Graph plotting
for i in range(6):
	
	#Size in the exponential order of 5
	size = size*2
	
	#Random array generation 
	randomList = random.sample(range(0,10000000), size)
	randomList.sort(reverse=True)
	sizeList.append(size)
	randomArray = np.array(randomList)
	
	#Start of Time evaluation
	start = time.time()
	
	#Return value form function call
	sortedArray = quickSort(randomArray)
	#If found
	print("Sorted array: ", sortedArray)

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
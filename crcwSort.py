import threading
import time
from timeit import default_timer as timer

global count
global totalCount
global arrangeSequence
global sortedSequence
global timeExecution
count = []
totalCount = []
arrangeSequence = []
sortedSequence = []
timeExecution = 0.0


def crcwSort(arr, iJ, TT):
	start = timer()
	for i in range(len(TT)): ## execute step 1
		TT[i].start()

	temp = 0
	for i in range(len(count)): ## get specific count
		temp += count[i][2]
		if((i+1)%len(arr)==0):
			totalCount.append(temp)
			temp = 0
	# print(totalCount)

	TT2 = []

	for i in range(len(arr)): ## thread create and execute step 2
		x = threading.Thread(target=step2, args=(i, arr,))
		x.start()
	# print(arrangeSequence)

	for i in range(len(arr)):
		sortedSequence.append(0)

	temp = 0
	for i in range(len(arr)):
		sortedSequence[arrangeSequence[i]] = arr[i]
		temp += 1
	# print(sortedSequence)
	end = timer()
	timeExecution = end-start




def step1(i, j, S):
	if((S[i]>S[j]) or (S[i]==S[j]) and i>j):
		count.append([i, j, 1])
		# print(i, j, 1)
	else:
		count.append([i, j, 0])
		# print(i, j, 0)


def step2(i, S):
	arrangeSequence.append(totalCount[i])

	

# arr = [1,2,3,1,2,1,3]

def crcwSortSchedule(arr):
	global count
	global totalCount
	global arrangeSequence
	global sortedSequence
	global timeExecution
	count = []
	totalCount = []
	arrangeSequence = []
	sortedSequence = []
	timeExecution = 0.0
	n = len(arr)
	iJ = []
	TT = []
	for t1 in range(1,n+1):
		for t2 in range(1,n+1):
			iJ.append([t1,t2])

	for i in range(len(iJ)):
		x = threading.Thread(target=step1, args=(iJ[i][0]-1, iJ[i][1]-1, arr,))
		TT.append(x)
	crcwSort(arr, iJ, TT)
	return(sortedSequence, timeExecution)



# print(crcwSortSchedule([5,2,4,5]))
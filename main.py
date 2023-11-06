from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import bubbleSort as bb
import selectionSort as se
import insertionSort as ins
import heapSort as he
import quickSort as qu
import mergeSort as me
import crcwSort as crcw
from timeit import default_timer as timer

# Window Position #
root = Tk()
root.title("SE-TC")
root.iconbitmap("Resources/icon.ico")
root.geometry("550x650+400+20")
root.resizable(False, False)
root.configure(bg="#3a1f8b")
###################

# Design Parts #
global upperFrame
global middleFrame
global lowerFrame
global calculationCoverFrame
global flag1
global top1
flag1 = True
upperFrame = Frame(root, bg="#3a1f8b")
middleFrame = Frame(root, bg="#3a1f8b")
lowerFrame = Frame(root, bg="#008080")
calculationCoverFrame = Frame(middleFrame, bg="#596add", width="510", height="150")

img = ImageTk.PhotoImage(Image.open("Resources/setc.png").resize((70,70)))
i = Label(upperFrame, image=img, bg="#3a1f8b")
i.image = img
i.grid(row=0, column=0, rowspan="3") # logo photo add

title = Label(upperFrame, text="Sorting Execution Time Calculator", bg="#3a1f8b", fg="white", font="Impact 22 bold")
title.grid(row=1, column=1) # logo title add

hr = Frame(upperFrame, width="320px", bg="yellow")
hr.grid(row=2, column=1)
hr = Frame(upperFrame, width="320px", bg="yellow")
hr.grid(row=0, column=1)


###### Calculation Area ##########
def numberArrange(n):	
	dotFirstNumber = n[:n.find('.')]
	dotSecondNumber = n[n.find('.')+1:n.find('e-')]
	ePowerNumber = int(n[n.find('e-')+2:])
	result = "0."
	for i in range(ePowerNumber-1):
		result = result+"0"
	result = result+dotFirstNumber+dotSecondNumber
	return(result)

def calculationShowFunction(sortType):
	global calculationCoverFrame
	calculationCoverFrame.destroy()
	calculationCoverFrame = Frame(middleFrame, bg="#596add", width="510", height="150")
	calculationCoverFrame.grid(row=7, column=0, columnspan=3, sticky=W, ipady=10, ipadx=10, pady=3)
	inputStr = userInput.get().strip().split() # get user input
	sortedArr = []
	if(sortType=="bubble" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Bubble Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = bb.bubbleSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)])
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n^2)")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)



	elif(sortType=="selection" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Selection Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = se.selectionSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n^2)")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)



	elif(sortType=="insertion" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Insertion Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = ins.insertionSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n^2)")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)



	elif(sortType=="heap" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Heap Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = he.heapSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n log(n))")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)



	elif(sortType=="quick" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Quick Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = qu.quickSortSchedule([eval(i) for i in inputStr], 0, len([eval(i) for i in inputStr])-1) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n^2)")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)


	elif(sortType=="merge" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for Merge Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="35", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="26", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = me.mergeSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(n log(n))")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)



	elif(sortType=="crcw" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for CRCW Model Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="40", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="[ "+str(len([eval(i) for i in inputStr]))+" ] index", width="20", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		sortedArr, run_time = crcw.crcwSortSchedule([eval(i) for i in inputStr]) # sorting
		sortedArr = ",".join([str(l) for l in (sortedArr)]) 
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t2var.set(sortedArr)
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t3var = StringVar()
		t3var.set("O(1)")
		t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t4var = StringVar()
		if ("e-" in str(run_time)):
			run_time = numberArrange(str(run_time))
		t4var.set(str(run_time) + " (s)")
		t6 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set(str(float(run_time)*1000) + " (ms)")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)
	elif(sortType=="crew" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for CREW Model Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="40", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="LATER DEVELOPMENT", width="20", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("LATER DEVELOPMENT")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t4var = StringVar()
		t4var.set("LATER DEVELOPMENT")
		t4 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t6var = StringVar()
		t6var.set("LATER DEVELOPMENT")
		t6 = Entry(calculationCoverFrame, textvariable=t6var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set("LATER DEVELOPMENT")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)
	elif(sortType=="erew" and all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		l1 = Label(calculationCoverFrame, text="Worse case time complexity for CREW Model Sort : ", font="Times 12 bold", bg="#596add", fg="white", width="40", anchor=W)
		l1.grid(row=0, column=0, columnspan=2, sticky=W, pady=3)
		l2 = Label(calculationCoverFrame, text="LATER DEVELOPMENT", width="20", font="Times 9 bold", bg="#596add", fg="yellow", anchor=E)
		l2.grid(row=0, column=2, sticky=E, pady=3)
		
		t1 = Label(calculationCoverFrame, text="Sorted array : ", font="Times 12 bold", bg="#596add", fg="white")
		t1.grid(row=1, column=0, sticky=W, pady=1)
		t2var = StringVar()
		t2var.set("LATER DEVELOPMENT")
		t2 = Entry(calculationCoverFrame, textvariable=t2var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t2.grid(row=1, column=1, columnspan=2, sticky=W, pady=1)

		t3 = Label(calculationCoverFrame, text="Time Complexity : ", font="Times 12 bold", bg="#596add", fg="white")
		t3.grid(row=2, column=0, sticky=W, pady=5)
		t4var = StringVar()
		t4var.set("LATER DEVELOPMENT")
		t4 = Entry(calculationCoverFrame, textvariable=t4var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t4.grid(row=2, column=1, columnspan=2, sticky=W, pady=1)

		t5 = Label(calculationCoverFrame, text="Execution time : ", font="Times 12 bold", bg="#596add", fg="white")
		t5.grid(row=3, column=0, sticky=W, pady=1)
		t6var = StringVar()
		t6var.set("LATER DEVELOPMENT")
		t6 = Entry(calculationCoverFrame, textvariable=t6var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t6.grid(row=3, column=1, columnspan=2, sticky=W, pady=2)

		t7var = StringVar()
		t7var.set("LATER DEVELOPMENT")
		t8 = Entry(calculationCoverFrame, textvariable=t7var, state="readonly", font="Times 12 bold", bg="#596add", fg="red", relief="solid", width="45")
		t8.grid(row=4, column=1, columnspan=2, sticky=W, pady=2)
	else:
		messagebox.showwarning("Warning", "Check your input value. [Format input >> 2 1 2 4 ... n]")


##################################


Label(middleFrame, text="Enter sequence of integer {\"0 0 0 0 ...\"}", bg="#3a1f8b", font="Times 13", fg="white").grid(row=0, column=0, sticky=W, pady=5, columnspan=3)
userInput = Entry(middleFrame, width="66", justify="left", relief="sunken", font="Times 12")
userInput.grid(row=1 , column=0, columnspan=3, sticky=W, pady=10) # Entry box added

############################
#------ Button Hover and flow right click ------#

def showFlowPhoto(e):
	global flag1
	global top1
	print(flag1)
	if(flag1):
		top1 = Toplevel()
		top1.geometry("+0+0")
		top1.configure(bg="white")
		top1.title(e.widget["text"]+" Flow Photo ")
		top1.iconbitmap("Resources/icon.ico")
		top1.resizable(False, False)
		tempPhoto = e.widget["text"]
		i1 = ImageTk.PhotoImage(Image.open("Resources/References/"+tempPhoto+".png"))
		fp = Label(top1, image=i1, anchor="nw", bg="#444487")
		fp.image = i1
		fp.pack()
		print("show flow"+ e.widget["text"])
		flag1 = False
	else:
		print("hide flow"+ e.widget["text"])
		flag1 = True
		top1.destroy()

def on_enter(e):
	bubbleSortButton = e.widget
	bubbleSortButton.configure(bg="#009877", fg="yellow", relief="raised", activeforeground="white", activebackground="#ff4545")
def on_leave(e):
	bubbleSortButton = e.widget
	bubbleSortButton.configure(bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545")

def show_image(event):
	global top
	top = Toplevel(lowerFrame)
	top.title("Group members")
	top.iconbitmap("Resources/icon.ico")
	top.geometry("+20+30")
	top.resizable(False, False)
	img = ImageTk.PhotoImage(Image.open("Resources/gp.png").resize((350,270)))
	l = Label(top, image=img)
	l.pack()
	l.image = img

def un_show_image(event):
	global top
	top.destroy()

def allCalculationSchedule():
	inputStr = userInput.get().strip().split() # get user input
	# print(inputStr)
	bbs, bbr = bb.bubbleSortSchedule([eval(i) for i in inputStr])
	ses,ser = se.selectionSortSchedule([eval(i) for i in inputStr])
	inss, insr = ins.insertionSortSchedule([eval(i) for i in inputStr])
	hes, her = he.heapSortSchedule([eval(i) for i in inputStr])
	qus, qur = qu.quickSortSchedule([eval(i) for i in inputStr], 0, len([eval(i) for i in inputStr])-1)
	mes, mer = me.mergeSortSchedule([eval(i) for i in inputStr])
	crs, crr = crcw.crcwSortSchedule([eval(i) for i in inputStr])
	if ("e-" in str(bbr)):
		bbr = numberArrange(str(bbr))
	if ("e-" in str(ser)):
		ser = numberArrange(str(ser))
	if ("e-" in str(insr)):
		insr = numberArrange(str(insr))
	if ("e-" in str(her)):
		her = numberArrange(str(her))
	if ("e-" in str(qur)):
		qur = numberArrange(str(qur))
	if ("e-" in str(mer)):
		mer = numberArrange(str(mer))
	if ("e-" in str(crr)):
		crr = numberArrange(str(crr))
	allCalculation(bbs, bbr, ser, insr, her, qur, mer, crr, inputStr)

def allCalculation(bbs, bbr, ser, insr, her, qur, mer, crr, inputStr):
	global top
	if(all([item.isdigit() for item in inputStr]) and len(inputStr)!=0):
		root.withdraw()
		top = Toplevel(root)
		top.title("All sorting execution time")
		top.iconbitmap("Resources/icon.ico")
		top.geometry("1000x400+20+30")
		top.resizable(False, False)
		top.configure(bg="grey")

		tvar = StringVar()
		tvar.set(inputStr)
		# t4 = Entry(calculationCoverFrame, textvariable=t3var, state="readonly", font="Times 12 bold", bg="#596add", fg="black", relief="solid", width="45")

		Label(top, text="All Sorting Execution Time records", font="Times 20 bold", bg="grey", fg="white").grid(row=0, column=0, columnspan=9, pady=10)
		Label(top, text="Input sequence", font="Times 12 bold", bg="grey", fg="white").grid(row=1, column=0, sticky=W, padx=20)
		Entry(top, textvariable=tvar, state="readonly", font="Times 12 bold", bg="white", fg="black", width="90").grid(row=1, column=1, sticky=W, padx=20, pady=5, columnspan=3)
		Label(top, text="Sorted sequence", font="Times 12 bold", bg="grey", fg="white").grid(row=2, column=0, sticky=W, padx=20)
		tvar2 = StringVar()
		tvar2.set(bbs)
		Entry(top, textvariable=tvar2, state="readonly", font="Times 12 bold", bg="white", fg="black", width="90").grid(row=2, column=1, sticky=W, padx=20, pady=5, columnspan=3)
		# Label(top, text=str(bbs), font="Times 12 bold", bg="white", fg="black").grid(row=2, column=1, sticky=W, padx=20, pady=5)
		Label(top, text="Bubble sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=3, column=0, sticky=W, padx=20)
		Label(top, text=str(bbr)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=3, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(bbr)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=3, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n^2)", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=3, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="Selection sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=4, column=0, sticky=W, padx=20)
		Label(top, text=str(ser)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=4, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(ser)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=4, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n^2)", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=4, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="InsertionSort sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=5, column=0, sticky=W, padx=20)
		Label(top, text=str(insr)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=5, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(insr)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=5, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n^2)", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=5, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="Heap sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=6, column=0, sticky=W, padx=20)
		Label(top, text=str(her)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=6, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(her)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=6, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n log(n))", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=6, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="Quick sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=7, column=0, sticky=W, padx=20)
		Label(top, text=str(qur)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=7, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(qur)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=7, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n^2)", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=7, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="Merge sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=8, column=0, sticky=W, padx=20)
		Label(top, text=str(mer)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=8, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(mer)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=8, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(n log(n))", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=8, column=3, sticky=W, padx=20, pady=5)
		Label(top, text="CRCW model sort run time", font="Times 12 bold", bg="grey", fg="white").grid(row=9, column=0, sticky=W, padx=20)
		Label(top, text=str(crr)+" (s)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=9, column=1, sticky=W, padx=20, pady=5)
		Label(top, text=str(float(crr)*1000)+" (ms)", font="Times 12 bold", bg="white", fg="black", width=30, anchor=W).grid(row=9, column=2, sticky=W, padx=20, pady=5)
		Label(top, text="O(1)", font="Times 12 bold", bg="white", fg="black", width=9, anchor=W).grid(row=9, column=3, sticky=W, padx=20, pady=5)
		def top_close():
			top.destroy()
			root.deiconify()
		top.protocol("WM_DELETE_WINDOW",top_close)
	else:
		messagebox.showwarning("Warning", "Check your input value. [Format input >> 2 1 2 4 ... n]")


############################

Label(middleFrame, text="**right click on button for sorting flow**", bg="#3a1f8b", font="Times 11", fg="grey").grid(row=2, column=0, columnspan=3, pady=2, sticky=W)

bubbleSortButton = Button(middleFrame, text="Bubble Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("bubble"))
selectionSortButton = Button(middleFrame, text="Selection Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("selection"))
insertionSortButton = Button(middleFrame, text="Insertion Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("insertion"))

heapSortButton = Button(middleFrame, text="Heap Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("heap"))
quickSortButton = Button(middleFrame, text="Quick Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("quick"))
mergeSortButton = Button(middleFrame, text="Merge Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("merge"))

crcwSortButton = Button(middleFrame, text="CRCW Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("crcw"))
crewSortButton = Button(middleFrame, text="CREW Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("crew"))
erewSortButton = Button(middleFrame, text="EREW Sort", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="22", command=lambda:calculationShowFunction("erew"))

compareAllSortButton = Button(middleFrame, text="Compare all sorting", font="Times 10 bold", bg="lightblue", fg="black", relief="groove", activeforeground="white", activebackground="#ff4545", width="73", command=allCalculationSchedule)

bubbleSortButton.grid(row=3, column=0, pady=8, ipadx=4, ipady=3, sticky=W)
selectionSortButton.grid(row=3, column=1, pady=8, ipadx=4, ipady=3)
insertionSortButton.grid(row=3, column=2, pady=8, ipadx=4, ipady=3, sticky=E)
heapSortButton.grid(row=4, column=0, pady=8, ipadx=4, ipady=3, sticky=W)
quickSortButton.grid(row=4, column=1, pady=8, ipadx=4, ipady=3)
mergeSortButton.grid(row=4, column=2, pady=8, ipadx=4, ipady=3, sticky=E)
crcwSortButton.grid(row=5, column=0, pady=8, ipadx=4, ipady=3, sticky=W)
crewSortButton.grid(row=5, column=1, pady=8, ipadx=4, ipady=3)
erewSortButton.grid(row=5, column=2, pady=8, ipadx=4, ipady=3, sticky=E)
compareAllSortButton.grid(row=6, column=0, columnspan=3, pady=8, ipadx=4, ipady=3)

bubbleSortButton.bind("<Enter>", on_enter)
bubbleSortButton.bind("<Leave>", on_leave)
selectionSortButton.bind("<Enter>", on_enter)
selectionSortButton.bind("<Leave>", on_leave)
insertionSortButton.bind("<Enter>", on_enter)
insertionSortButton.bind("<Leave>", on_leave)
heapSortButton.bind("<Enter>", on_enter)
heapSortButton.bind("<Leave>", on_leave)
quickSortButton.bind("<Enter>", on_enter)
quickSortButton.bind("<Leave>", on_leave)
mergeSortButton.bind("<Enter>", on_enter)
mergeSortButton.bind("<Leave>", on_leave)
crcwSortButton.bind("<Enter>", on_enter)
crcwSortButton.bind("<Leave>", on_leave)
crewSortButton.bind("<Enter>", on_enter)
crewSortButton.bind("<Leave>", on_leave)
erewSortButton.bind("<Enter>", on_enter)
erewSortButton.bind("<Leave>", on_leave)
compareAllSortButton.bind("<Enter>", on_enter)
compareAllSortButton.bind("<Leave>", on_leave)
bubbleSortButton.bind("<Button-3>",showFlowPhoto)
selectionSortButton.bind("<Button-3>",showFlowPhoto)
insertionSortButton.bind("<Button-3>",showFlowPhoto)
heapSortButton.bind("<Button-3>",showFlowPhoto)
quickSortButton.bind("<Button-3>",showFlowPhoto)
mergeSortButton.bind("<Button-3>",showFlowPhoto)
crcwSortButton.bind("<Button-3>",showFlowPhoto)
crewSortButton.bind("<Button-3>",showFlowPhoto)
erewSortButton.bind("<Button-3>",showFlowPhoto)


footer1 = Label(lowerFrame, text="+  Project report for Analysis Algorithms", font="Times 10 bold italic",bg="#008080", fg="white", width="72", anchor=W, height="1")
footer2 = Label(lowerFrame, text="+  Copyright by group [1], fifth year", font="Times 10 bold italic",bg="#008080", fg="white", width="72", anchor=W, cursor="hand2")
footer3 = Label(lowerFrame, text="+  University of Computer Studies Sittwe", font="Times 10 bold italic",bg="#008080", fg="white", width="72", anchor=W, height="1")

footer1.grid(row=0, sticky=W)
footer2.grid(row=1, sticky=W)
footer3.grid(row=2, sticky=W)

upperFrame.grid(row=0, padx=10, pady=10)
middleFrame.grid(row=1, padx=10)
lowerFrame.grid(row=2, padx=10, pady=10, ipadx=11)
calculationCoverFrame.grid(row=7, column=0, columnspan=3, sticky=W, ipady=10, ipadx=10, pady=3)


footer2.bind("<Enter>",show_image)
footer2.bind("<Leave>",un_show_image)
#####

root.mainloop()
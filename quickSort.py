from timeit import default_timer as timer

arr = []
low = 0
high = 0

def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

# sort
def quickSort(arr,low,high):
   if low < high:
      # index
      pi = partition(arr,low,high)
      # sort the partitions
      try:
         quickSort(arr, low, pi-1)
         quickSort(arr, pi+1, high)
      except:
         pass
   return arr

def quickSortSchedule(arr,low,high):
    start = timer()
    tempSort = quickSort(arr,low,high)
    end = timer()
    return(arr, end-start)
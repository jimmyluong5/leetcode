#you keep dividing the array in half and sort the single index numbers in blocks
#eg [1, 5, 2, 9]
#[1] [5] [2] [9]
# [1, 5] [2, 9]
# [1, 2, 5, 9]

#this is a recursive sorting algo
#you break the array into sub problems that sort each sub problem then build it back up
#the subproblems are solved then put together.
#divide and conquer algorithm

#merge sort is O( nlog(n) )

#general principle
#1 split array in half
#2 call merge sort on each half to sort them recursively
#3 merge both sorted halves into one sorted array

#we know that we start with a large array and have to cut it in half
#so we need a left array and right array
arr = [2, 1, 5, 7, 22, 19, 2, 6, 4, 9, 10, 7, 21, 29, 76]
def MergeSort(arr):
    if len(arr) <=1:
        return arr
    #starting condition, we can only sort if we have more than 1 element, if 1 element then its already sorted
    else: #len(arr) > 1:

        #make the middle pointer
        mid = len(arr)//2

        #create the left and right array
        left_arr = arr[0:mid] #means from 0 to mid index.
        right_arr = arr[mid:len(arr)] #means from mid to the end index.

    #recursion call MergeSort on the left and right arrays
    MergeSort(left_arr)
    MergeSort(right_arr)

    #merge step
    #recall that we want to compare the left most element in the left and right arrays

    #indices to keep track of the elements for the arrays
    i = 0 #left arr idx
    j = 0 #right arr idx

    k = 0 #merge array index.
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            #then we save the value in our merged array arr
            arr[k] = left_arr[i]
            #then increment left index and k index
            k+=1
            i+=1
        else:
            #the values in the right array are smaller so we add that element first to
            #the merged array
            arr[k] = right_arr[j]
            #increment pointers
            k+=1
            j+=1
        #or you can factor out k+=1 and put it here doesn't matter really.
    
    #if we have finished merging all the elements in the left array to the merged array
    #then we must append the rest of the elements in the right array in the merged array
    while j < len(right_arr):
        arr[k] = right_arr[j]
        k+=1
        j+=1

    #if we placed all the elements in the right array already, we just need to put the elements
    #in the left array into the merged array
    while i < len(left_arr):
        arr[k] = left_arr[i]
        k+=1
        i+=1

    return arr #return the sorted array

print(MergeSort(arr))





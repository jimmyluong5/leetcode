#we are going to implement quicksort, this sorting algo sorts in place unlike mergesort


def quicksort(arr, left, right): #inputs are the arr itself
    #and the left and right pointers 
    if left < right: #make sure our pointers are in the proper place
        #we need to get the pivot index
        pi = partition(arr, left, right)

        #sort the left and right array

        #left array
        quicksort(arr, left, pi-1)
        
        #right array
        quicksort(arr, pi+1, right)

    return arr #return the sorted array

#this function is to take the subarray and sort it in a way where all the elements
#less than the pivot value is on the left of the pivot

#values greater of the pivot value are right of the pivot
#returns the index of the pivot value.
def partition(arr, left, right):

#choose the last element as the pivot
    pivot = arr[right]

    #create the ptrs for iterating and moving
    #left and right act as boundaries or walls for the ptrs
    i = left
    j = right-1

    while i < j:
        while i < right and arr[i] < pivot: #move the i ptr if 
            #our value is less than the pivot value
            i+=1
        while j > left and arr[j] >= pivot:
            #move the j ptr if our value is greater than the pivot value
            j-=1

        #after the while loops run, if we hit this part of code, we have found elements on each side
        #that are out of place such as an element larger than pivot on left side
        #element smaller than pivot on right side
        if i < j:  
            #we need to swap and move the ptrs
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    #if the j index is ahead of the i index then we need to swap the value at the (i) index and pivot value
    if arr[i] > pivot: #like if we see a value in the left subarray greater than pivot we gotta swap.
        #we need to swap the pivot value with the value at (i)
        #the pivot value is set at right.
        arr[i], arr[right] = arr[right], arr[i]
    return i #this is the pivot index.


arr = [1,2,56,7,12,3,6,3,12,3,5,2,1,5,66,7,8,19,2,5,1,4,2,5,6,12,4,56]
print(quicksort(arr, 0, len(arr)-1))

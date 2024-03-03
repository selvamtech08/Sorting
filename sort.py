from typing import List


class Sort:
    """Sorting algorithms implementation"""
    @staticmethod
    def selection_sort(arr: List[int]) -> List[int]:
        """Selection sort technique
            moving min value at left in each iteration
        """
        #traverse the elements one by one
        for i in range(len(arr)):   
            #assume ith element a min at start of traverse inner loop like placeholder
            min_index = i           
            #traverse from ith index to end
            for j in range(i+1, len(arr)):    
                #compare ith element with jth values(next subsequent elements from i+1)
                #if jth element is less then reassign min index value
                if arr[j] < arr[min_index]:   
                    #reassign the min index position
                    min_index = j               
            #swap the ith and min index values
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp
        #Return sorted list
        return arr

    @staticmethod
    def bubble_sort(arr: List[int]) -> List[int]:
        """Bubble sort algorithm implemention
            Move max value at right in each iteration
        """
        #traverse the list
        for i in range(len(arr)):           
            #traverse the list items and reduce the last index postion by one in each iteration
            #because maximum item will be moved at end of list in each iteration
            for j in range(len(arr)-1):     
                #compare if jth value is greater than its next value (cond:1)
                if arr[j] > arr[j+1]:
                    #swap the elements if cond:1 matched
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        #return sorted list
        return arr

    @staticmethod
    def insertion_sort(arr: List[int]) -> List[int]:
        """Insertion sorting algorithm
            traverse the elements one by one
            compare current i-th value with previous elements and move ith value to correct order
        """
        #traverse the array from 1-index to end
        for i in range(1, len(arr)):
            #traverse the array from ith to 0 index (reverse order)
            for j in range(i,0,-1):
                #compare j-1 greater then j (current vs previous element) 
                if arr[j-1] > arr[j]:
                    #if yes swap the jth element to previous place
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp                
        #Return sorted value
        return arr

    @staticmethod
    def __merge_items(first: List[int], second: List[int]) -> List[int]:
        #initial the variable for iteration purpose
        x = y = z = 0
        #array for store result
        result: List[int] = [] 
        #Traverse the first and second arrays until reached at end     
        while x < len(first) and y < len(second):
            #if x-index first element is less then y-index second
            if first[x] < second[y]:
                #add x element from first array
                result.append(first[x])
                #increment x(first), z(result)
                x += 1
                z += 1
            else:
                #add y element from second array
                result.append(second[y])
                #increment y(second), z(result)
                y += 1
                z += 1            
        #check whether element left in the arrays if not traversed in previous condition 
        for i in range(x, len(first)):
            result.append(first[i])
        for i in range(y, len(second)):
            result.append(second[i])
        #Result result array
        return result

    @staticmethod
    def merge_sort(arr: List[int]) -> List[int]:
        """Merge sorting algorithm
            divide the array and conquer(rejoin) the elements back 
            i.e, split as sub-arrays(half of elements on left and right side) as much possible up-to single element at each array(length as 1)
            rejoin the sub-array in sorted order in recurse manner.
        """
        #recursion call break if reached at single element array
        if len(arr) == 1:
            return arr
        #find medium value to split the array as two part
        mid: int = len(arr) // 2
        #left half of element from current arr values
        #because recursion call happens   
        left = Sort.merge_sort(arr[0:mid])
        #right half of element from current arr values
        right = Sort.merge_sort(arr[mid:])
        #once divide complement, next join the arrays to combine single array
        #return the array
        return Sort.__merge_items(left, right)

    @staticmethod
    def __quicksort(arr: List[int], low: int, high: int) -> List[int]:
        #recursive call end
        if low >= high:
            return 
        #split the array into to sub-array based on pivot position
        start = low
        end = high
        #middle index to assign pivot 
        mid = (start + end) //2
        #traverse until start and end reached at same index
        while start <= end:
            #reassign pivot for current function call
            pivot = arr[mid]
            #find out if any element from leftside greater than pivot
            #if no increment the index by one
            while arr[start] < pivot:
                start += 1
            #find out if any element from rightside less than pivot
            #if no decrement the index by one                
            while arr[end] > pivot:
                end -= 1
            #if start and end not reached at same position then swap the elements                                 
            if start <= end:
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start +=1
                end -= 1        
        #pass both arrays to same function again until it reached low reached to high position 
        Sort.__quicksort(arr, low, end)
        Sort.__quicksort(arr, start, high)

    @staticmethod
    def quick_sort(arr: List[int]) -> List[int]:
        """Quick sort algorithm
            Choose one element in each iteration and move that element to correct order by traverse the array
            pivot will be calculated from middle of array
        """
        #inner function to call recursively 
        Sort.__quicksort(arr, 0, len(arr)-1)
        return arr

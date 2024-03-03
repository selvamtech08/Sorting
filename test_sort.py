from time import perf_counter
import random

from sort import Sort

#random_list = [3, 8, 1, 6]
random_list = [2, 5, 8, 1, -7, 0, 15, 3, 7, 6, 9, 14, 23, 27, 16]
#random_list = [random.randint(1,10000) for i in range(5000)]

print("Selection sort")
start = perf_counter()
select_result = Sort.selection_sort(random_list)
end = perf_counter()
print("Time taken:", end-start)

print("Bubble sort")
start = perf_counter()
bubble_result = Sort.bubble_sort(random_list)
end = perf_counter()
print("Time taken:", end-start)

print("Inserting sort")
start = perf_counter()
insert_result = Sort.insertion_sort(random_list)
end = perf_counter()
print("Time taken:", end-start)

print("Merge sort")
start = perf_counter()
merge_result = Sort.merge_sort(random_list)
end = perf_counter()
print("Time taken:", end-start)

print("Quick sort")
start = perf_counter()
quick_result = Sort.quick_sort(random_list)
end = perf_counter()
print("Time taken:", end-start)

print(select_result)
print(bubble_result)
print(insert_result)
print(merge_result)
print(quick_result)

if not select_result == bubble_result == insert_result == merge_result == quick_result:
    print("Sorting have bug")

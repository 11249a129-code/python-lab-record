//aim:to implement insetion sort and merge sort

//algorithm
Start from the 2nd element (index 1) of the list.
2. Save the value of the current element as key.
3. Compare the key with elements before it.
4. Shift all elements greater than key one position ahead.
5. Insert the key at the correct position.
6. Repeat for all elements in the list.

If the list has 0 or 1 element → already sorted.
2. Divide the list into two halves: left and right.
3. Recursively apply merge sort on each half.
4. Merge the two sorted halves:
Compare the elements from both halves.
Insert the smaller one into the result list.
5. Continue until all elements are merged.

//program
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are > key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element right
            j -= 1
        arr[j + 1] = key  # Insert key at correct position
    return arr
lst = [12, 11, 13, 5, 6]
print("Insertion Sort Result:", insertion_sort(lst))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]     
        right = arr[mid:]    
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += l
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
lst = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort Result:", merge_sort(lst))

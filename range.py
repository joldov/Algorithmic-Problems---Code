from typing import List

def range_count(A: List[int], x: int, y: int) -> int:
    def find_left_index(arr, target): #helper func 1 that finds the leftmost (first) index at which target could be inserted without violating the order of arr
        left = 0 
        right = len(arr) # defining the range within which we'll be searching for target
        while left < right: # loops as long as theres still a range to search within
            mid = left + (right - left) // 2 # dividing the range into 2 
            if arr[mid] < target: 
                left = mid + 1 # if mid is less than target, target must be in the right so we adjust left = mid + 1
            else:
                right = mid # else target is either at mid or in the left range, setting right = mid narrows search to the left half
        return left # left will be at the first index where target could be inserted into arr
    
    def find_right_index(arr, target): #helper func 2 to find the index just past the last occurrence of y in A
        left = 0
        right= len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else: 
                right = mid
        return left

    left_index = find_left_index(A, x)
    right_index = find_right_index(A, y)
    return right_index - left_index

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start = 1
        end = len(arr) - 2
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid - 1] < arr[mid]:  # Increasing side.......
                start = mid + 1
            else:  # Decreasing side........
                end = mid - 1
                
        return -1
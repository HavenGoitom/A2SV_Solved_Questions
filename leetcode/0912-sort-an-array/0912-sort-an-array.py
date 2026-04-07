class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_arr, right_arr):
            merged = []
            i = j = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    merged.append(left_arr[i])
                    i += 1
                else:
                    merged.append(right_arr[j])
                    j += 1
                    
            merged.extend(left_arr[i:])
            merged.extend(right_arr[j:])
            return merged

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            left_val = mergeSort(left, mid, arr)
            right_val = mergeSort(mid + 1, right, arr)

            return merge(left_val, right_val)
        
        return mergeSort(0, len(nums)-1, nums)
        
        return nums
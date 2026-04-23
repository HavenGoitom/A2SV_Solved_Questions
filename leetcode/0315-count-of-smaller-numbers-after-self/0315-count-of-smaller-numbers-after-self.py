class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # FIX: store value + index
        arr = [(nums[i], i) for i in range(n)]

        def merge(left_arr, right_arr):
            merged = []
            i = j = 0
            count = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i][0] <= right_arr[j][0]:
                    merged.append(left_arr[i])
                    res[left_arr[i][1]] += count
                    i += 1
                else:
                    count += 1
                    merged.append(right_arr[j])
                    j += 1
                    
            while i < len(left_arr):
                res[left_arr[i][1]] += count
                merged.append(left_arr[i])
                i += 1

            while j < len(right_arr):
                merged.append(right_arr[j])
                j += 1

            return merged

        def mergeSort(left, right):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            left_val = mergeSort(left, mid)
            right_val = mergeSort(mid + 1, right)

            return merge(left_val, right_val)
        
        mergeSort(0, n - 1)
        return res
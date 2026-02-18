class Solution:
    def relativeSortArray(self, arr1, arr2):
        
        rank = {}

        for i in range(len(arr2)):
            rank[arr2[i]] = i

        def customComparator(x):
            return (rank[x] if x in rank else len(arr2), x)

        arr1.sort(key=customComparator)
        return arr1

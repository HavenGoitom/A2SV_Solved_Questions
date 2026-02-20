class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # think of the papers as numbered 1, 2, 3… after sorting. 
        #Then for each paper: citation ≥ rank(i) 
        citations.sort(reverse=True)  
        n = len(citations)
        
        left = 0
        right = 0  
        count = 0  

        while right < n:
            papers_considered = right + 1  
            if citations[right] >= papers_considered:
                count = papers_considered  
            else:
                break
            right += 1

        return count
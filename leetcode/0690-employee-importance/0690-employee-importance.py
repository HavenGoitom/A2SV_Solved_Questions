"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        hashmap = {}
        for emp in employees:
            hashmap[emp.id] = [emp.importance, emp.subordinates]

        # print(hashmap) {1: [5, [2, 3]], 2: [3, []], 3: [3, []]}
        count = 0

        stack = []

        for emp in employees:
            if emp.id == id:
                stack.append(id)       
                break

        while stack:

            id = stack.pop()
            val = hashmap[id]
            count += val[0]

            if val[1]:
                for id2 in val[1]:
                    stack.append(id2)
            
        
        return count
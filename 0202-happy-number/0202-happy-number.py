class Solution:
    def isHappy(self, n: int) -> bool:
        
        happy_map = {
            "1": True,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": True,
            "8": False,
            "9": False
        }
        n_str = str(n)
        sum_of_num = 0
        while(True):
            sum_of_num = 0
            
            for i in range(len(n_str)):
                sum_of_num += (int(n_str[i])**2)

            if str(sum_of_num) in happy_map:
                return happy_map[str(sum_of_num)]
            n_str = str(sum_of_num)
            
                

        

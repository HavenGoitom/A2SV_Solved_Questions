class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(nums, alice, bob,turn):
            if len(nums) == 0:
                return alice >= bob
            
            if turn == 'A':
                new_alice = nums[0] + alice
                new_turn = 'B'

                if helper(nums[1:], new_alice, bob, new_turn):
                    return True

                new_alice = nums[-1] + alice
                if helper(nums[:len(nums)-1], new_alice,bob,new_turn):
                    return True

                return False

            else:
                new_bob = nums[0] + bob
                new_turn = 'A'

                if not (helper(nums[1:], alice, new_bob, new_turn)): # bob wins
                    return False

                new_bob = nums[-1] + bob
                if not (helper(nums[:len(nums)-1], alice, new_bob, new_turn)):
                    return False

                return True
                    
        return helper(nums,0,0,'A')
            


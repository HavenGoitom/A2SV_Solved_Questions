class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(nums, alice, bob,turn):
            if len(nums) == 0:
                return alice >= bob
            
            ans = True
            if turn == 'A':
                ans = False
                new_alice = nums[0] + alice
                new_turn = 'B'

                ans = ans or helper(nums[1:], new_alice, bob, new_turn)

                new_alice = nums[-1] + alice
                ans = ans or helper(nums[:len(nums)-1], new_alice,bob,new_turn)

            else:
                new_bob = nums[0] + bob
                new_turn = 'A'

                ans = ans and helper(nums[1:], alice, new_bob, new_turn)

                new_bob = nums[-1] + bob
                ans = ans and helper(nums[:len(nums)-1], alice, new_bob, new_turn)
                    
            return ans

        return helper(nums,0,0,'A')
            


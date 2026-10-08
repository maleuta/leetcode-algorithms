from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_map = set(nums)
        max_seq = 0

        for num in hash_map:
            if (num-1) not in hash_map:

                curr_num = num
                seq = 1

                while (curr_num+1) in hash_map:
                    seq += 1
                    curr_num = curr_num + 1

                if seq > max_seq:
                    max_seq = seq    

            
        
        return max_seq



print(Solution().longestConsecutive([2,20,4,10,3,4,5]))



            


        
# https://leetcode.com/problems/remove-element/submissions/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=nums.count(val)
        while c!=0:
            c=c-1
            nums.remove(val)
        length=len(nums)
        print(length)
        

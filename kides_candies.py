# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boollist=[]
        maxi=0
        maxi=max(candies)
        for i in candies:
            if(i+extraCandies>=maxi):
                boollist.append(True)
            else:
                boollist.append(False)
        return boollist

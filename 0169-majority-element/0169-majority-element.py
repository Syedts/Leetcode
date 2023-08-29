class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        check = len(nums)/2
        res, maxCount = 0 , 0
        for n in nums:
            d[n] = d.get(n,0) + 1
            res = n if d[n] > maxCount else res
            maxCount = max(d[n],maxCount)

        return res
        
      
       
        

        


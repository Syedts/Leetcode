class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d ={}
        check = len(nums)/2
        for n in nums:
            d[n] = d.get(n,0) + 1
        
        for num, count in d.items():
            if count > check:
                return num
       
        

        


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var dict = {}
    for( let i = 0; i < nums.length;i++)
    {
        const currentNum = nums[i];
        const complement = target - currentNum;

        if( dict.hasOwnProperty(complement)) // If it exists
        {
            return [dict[complement], i];
        }
        dict[currentNum] = i
    }
    return [];
};

/*
         lookup = {}
        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]],i]
            else:
                lookup[target-nums[i]] = i

        return None 

*/
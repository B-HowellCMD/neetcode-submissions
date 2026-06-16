class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index ## we need to initiize an empty hashmap so we can compare values

        # we want to go through our map (enumerate) and we want to do that with nums <-- nums is declared as our list
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

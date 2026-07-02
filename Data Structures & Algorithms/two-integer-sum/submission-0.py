class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        r=[]
        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                r.append(seen[need]) 
                r.append(i)

            seen[nums[i]] = i
        return r
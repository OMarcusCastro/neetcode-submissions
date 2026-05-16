class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        cache2 = {}
        for i in range(len(nums)):
            
            cache[nums[i]] = target-nums[i]
            cache2[nums[i]]=i
        ans = []
        for i in range(len(nums)):
            # print(nums[i])
            if cache.get(target-nums[i]) == nums[i] and i  != cache2[target-nums[i]] :
                ans.append(i)
                ans.append(cache2[target-nums[i]])
                break

        return ans


            

        
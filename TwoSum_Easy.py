#THe below is a brute force solution takes lot of time but does the job with lil less memory
#  class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         arrLen = len(nums)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[i] + nums[j] == target):
#                     return [nums.index(i), nums.index(j)]

#The below one is a faster one but uses large memory
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
                """
        myDict = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in myDict:
                return myDict[complement], i
            myDict[nums[i]] = i


ipArr = [3, 3]
ip = 6
newInstance = Solution()
ans = newInstance.twoSum(ipArr, ip)
print(ans)

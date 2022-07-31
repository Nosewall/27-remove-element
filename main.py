class Solution:
    def removeElement(self, nums, val) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1

        print(nums)
        return len(nums)

sol = Solution()
arr = [3,2,2,3]
v = 3
sol.removeElement(arr, v)

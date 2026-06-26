class Solution:
   
    def moveZeroes(self, nums: List[int]) -> None:
        t = []

        for num in nums:
            if num != 0:
                t.append(num)

        while len(t) < len(nums):
            t.append(0)

        nums[:] = t
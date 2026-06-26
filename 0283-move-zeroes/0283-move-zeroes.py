class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                """" this is the simple approach
                def moveZeroes(self, nums: List[int]) -> None:
                    t = []

                    for num in nums:
                        if num != 0:
                        t.append(num)

                    while len(t) < len(nums):
                            t.append(0)

                    nums[:] = t"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:  # rotação à direita
                left = mid + 1
            else:                         # mínimo à esquerda (inclui mid)
                right = mid

        return nums[left]
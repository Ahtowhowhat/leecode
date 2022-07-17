class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=nums[low]:
                if nums[mid]>nums[high]:
                    low = mid+1
                else:
                    return nums[low]
            elif nums[mid]<nums[high]:
                if nums[mid]<nums[low]:
                    high = mid
                else:
                    return nums[low]
        return nums[low]


class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]<nums[high]:
                high = mid
            else:
                low = mid+1
        return nums[low]
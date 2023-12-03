def rearrange_nums(nums):
    if len(nums) <= 1:
        return nums
    
    if nums[0] % 2 == 0:
        return [nums[0] + rearrange_nums(nums[1:])]
    else:
        return rearrange_nums(nums[1:]) + [nums[0]]
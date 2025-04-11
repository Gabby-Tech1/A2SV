def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)

    count_smaller = {}
    for i, num in enumerate(sorted_nums):
        if num not in count_smaller:
            count_smaller[num] = i
    
    result = [count_smaller[num] for num in nums]
    
    return result
    
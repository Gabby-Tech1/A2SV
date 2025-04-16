def largestNumber(nums):
    """
    Given a list of non-negative integers, arrange them such that they form the largest number possible.
    
    :param nums: List of non-negative integers
    :return: The largest number formed by the integers in the list as a string
    """
    # Convert all numbers to strings for easier comparison
    nums = list(map(str, nums))
    
    # Sort numbers based on custom comparison
    nums.sort(key=lambda x: x * 10, reverse=True)
    
    # Join sorted numbers into a single string
    largest_num = ''.join(nums)
    
    # Handle edge case where the result is all zeros
    return largest_num if largest_num[0] != '0' else '0'
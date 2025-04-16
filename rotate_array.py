def rotate(nums, k):
    """
    Rotate the array nums to the right by k steps, where k is non-negative.
    
    :param nums: List[int] - The list of integers to rotate.
    :param k: int - The number of steps to rotate the array.
    :return: None - The function modifies nums in place.
    """
    n = len(nums)
    k %= n  # Handle cases where k is greater than n
    nums[:] = nums[-k:] + nums[:-k]  # Rotate the array in place
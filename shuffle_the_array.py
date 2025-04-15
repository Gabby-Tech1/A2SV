def shuffle(nums, n):
    """
    Shuffle the array nums of length 2n so that the shuffled array is [x1,y1,x2,y2,...,xn,yn].

    :param nums: List[int] - The input array of length 2n.
    :param n: int - The number of pairs in the input array.
    :return: List[int] - The shuffled array.
    """
    res = []

    for i in range(2*n):
        if i % 2 == 0:
            res.append(nums[i // 2])
        else:
            res.append(nums[n + i // 2])
            
    return res
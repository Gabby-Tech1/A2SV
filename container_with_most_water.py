def maxArea(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        width = right - left
        area = min(heights[left], heights[right]) * width
        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
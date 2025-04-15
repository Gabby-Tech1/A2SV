def judgeSquareSum(c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        if c == 0:
            return True
        
        left, right = 0, int(c**0.5)
        while left <= right:
            total = left ** 2 + right ** 2
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        return False
def totalFruits(fruits):
    left = 0
    right = 0
    max_fruits = 0
    fruit_count = {}

    while right < len(fruits):
        if fruits[right] in fruit_count:
            fruit_count[fruits[right]] += 1
        else:
            fruit_count[fruits[right]] = 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)
        right += 1

    return max_fruits
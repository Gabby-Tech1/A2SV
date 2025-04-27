def totalFruits(fruits):
    left = 0
    right = 0
    max_fruits = 0
    fruit_count = {}

    while right < len(fruits):
        # Add the current fruit to the basket
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

        # If we have more than 2 types of fruits, move the left pointer
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        # Update the maximum number of fruits in the basket
        max_fruits = max(max_fruits, right - left + 1)
        right += 1

    return max_fruits
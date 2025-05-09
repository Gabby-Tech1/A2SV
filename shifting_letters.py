def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    shift_count = [0] * (n + 1)

    for start, end, direction in shifts:
        if direction == 1:
            shift_count[start] += 1
            if end + 1 < n:
                shift_count[end + 1] -= 1
        else:  # Left shift
            shift_count[start] -= 1
            if end + 1 < n:
                shift_count[end + 1] += 1

    # Calculate the cumulative shifts
    current_shift = 0
    for i in range(n):
        current_shift += shift_count[i]
        # Normalize the shift to be within the range of [0, 25]
        normalized_shift = current_shift % 26
        # Shift the character and wrap around using modulo
        s = s[:i] + chr((ord(s[i]) - ord('a') + normalized_shift) % 26 + ord('a')) + s[i+1:]

    return s


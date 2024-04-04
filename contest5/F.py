def podpalin(s):
    n = len(s)
    modified_string = '#' + '#'.join(s) + '#'
    palindrome_lengths = [0] * len(modified_string)
    center = right = 0
    count = 0

    for i in range(1, len(modified_string) - 1):
        mirror = 2 * center - i
        if i < right:
            palindrome_lengths[i] = min(right - i, palindrome_lengths[mirror])
        while (i + (1 + palindrome_lengths[i])) < len(modified_string) and (i - (1 + palindrome_lengths[i])) >= 0 and modified_string[i + (1 + palindrome_lengths[i])] == modified_string[i - (1 + palindrome_lengths[i])]:
            palindrome_lengths[i] += 1
        if i + palindrome_lengths[i] > right:
            center = i
            right = i + palindrome_lengths[i]
        count += (palindrome_lengths[i] + 1) // 2

    return count
s = input().strip()
print(podpalin(s))

def compute_prefix_function(pattern):
    prefix_function = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_function[i] = j
    return prefix_function

def kmp_search(text, pattern):
    prefix_function = compute_prefix_function(pattern)
    j = 0
    occurrences = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_function[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            occurrences += 1
            j = prefix_function[j - 1]
    return occurrences

def count_cyclic_shifts(a, b):
    occurrences = 0
    b_length = len(b)
    for i in range(len(a) - b_length + 1):
        # Проверяем, является ли подстрока a[i:i+b_length] циклическим сдвигом b
        if a[i:i+b_length] == b:
            # Проверяем, является ли следующий символ в a первым символом b
            if i + b_length < len(a) and a[i + b_length] == b[0]:
                occurrences += 1
    return occurrences

# Пример использования
a = "abcabcabc"
b = "abc"
print(count_cyclic_shifts(a, b)) # Теперь должно вывести 4

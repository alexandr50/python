src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [num for i, num in enumerate(src) if num[i] > src[i - 1] and num != 0]
print(result)

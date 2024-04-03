def minSubsequenceCount(source, target):
    s_len = len(source)
    t_len = len(target)
    i = 0
    lasti = -1
    count = 0
    while i < t_len and i > lasti:
        lasti = i
        for j in range(0, s_len):
            if i < t_len and source[j] == target[i]:
                i = i + 1
        count = count + 1
    if i != t_len:
        return -1
    else:
        return count


source = input("source = ")
target = input("target = ")
result = minSubsequenceCount(source, target)
print("output = ", result)

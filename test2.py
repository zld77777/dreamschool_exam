def checkParentheses(s):
    length = len(s)
    stack = []
    result = [" "] * length
    for i in range(0, length):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
    for c in stack:
        if s[c] == '(':
            result[c] = 'x'
        elif s[c] == ')':
            result[c] = '?'
    return result

str = input()
result = "".join((checkParentheses(str)))
print(str)
print(result)

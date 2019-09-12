# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in s:
        if not stack:
            stack.append(char)
        elif char not in table:
            stack.append(char)
        elif table[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return "NO"
    else:
        return "YES"    

if __name__ == '__main__':
    brackets = input()
    print(isBalanced(brackets))

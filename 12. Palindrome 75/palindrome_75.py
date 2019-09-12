def palindrome(s):
    s = s.lower()
    substrings = [s[i:j] for i in range(len(s)+1) for j in range(i+1, len(s)+1)]

    print(substrings)
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    print(palindromes)
    answer = len(max(palindromes, key=len)) - 1
    print(answer)

if __name__ == '__main__':
    s = input()
    palindrome(s)


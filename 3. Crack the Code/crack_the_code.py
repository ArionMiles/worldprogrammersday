def crack(code):
    return "".join(str(ord(char)) for char in code)

if __name__ == '__main__':
    code = input()
    print(crack(code))
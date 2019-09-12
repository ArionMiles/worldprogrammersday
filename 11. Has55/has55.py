def has55(l):
    return any(True for i in range(len(l)-1) if l[i] == 5 and l[i+1] == 5)

if __name__ == '__main__':
    # n = int(input())
    # l = []
    # for _ in range(n):
    #     elem = int(input())
    #     l.append(elem)
    l = [5, 5, 1, 3]
    if has55(l):
        print("true")
    else:
        print("false")
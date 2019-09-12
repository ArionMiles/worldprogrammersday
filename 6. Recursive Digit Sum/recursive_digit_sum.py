# Complete the superDigit function below.
def superDigit(n, k):
    answer = int(n) * k % 9
    return answer if answer else 9

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    print(superDigit(n, k))
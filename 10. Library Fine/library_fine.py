# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2 > y1:
        fine = 0
    elif y1 > y2:
        fine = 10000
    elif m1 < m2:
        fine = 0
    elif m1 > m2:
        fine = 500 * (m1 - m2)
    elif d1 < d2:
        fine = 0
    else:
        fine = 15 * (d2 - d1)
    return fine
    

if __name__ == '__main__':

    # d1M1Y1 = input().split()

    # d1 = int(d1M1Y1[0])

    # m1 = int(d1M1Y1[1])

    # y1 = int(d1M1Y1[2])

    # d2M2Y2 = input().split()

    # d2 = int(d2M2Y2[0])

    # m2 = int(d2M2Y2[1])

    # y2 = int(d2M2Y2[2])
    d1 = 5
    m1 = 5
    y1 = 2014
    d2 = 23
    m2 = 2
    y2 = 2014
    
    print(libraryFine(d1, m1, y1, d2, m2, y2))


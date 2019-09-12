def a(store):
    for _, v in store.items():
        count = 0
        N = v[2]
        height_reached = 0
        for _ in range(N):
            height_reached += v[0] # x
            if height_reached >= N:
                count += 1
                break
            height_reached -= v[1] # y
            
            count += 1
        print(count)
        
            

if __name__ == '__main__':
    T = int(input())
    store = {}
    for i in range(T):
        x, y, N = list(map(int, input().split()))
        store[i] = [x, y , N]
    
    a(store)

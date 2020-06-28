
for _ in range(int(input())):
    # x, y, n = input()
    x, y, n = map(int, input().split())
            
 
    for i in reversed(range(1, n)):
        k = x * i + y
    
        if k % x == y and k <= n:
            print(k)
            break
        
print(0)
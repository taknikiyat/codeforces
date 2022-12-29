# https://codeforces.com/problemset/problem/50/A
# O()t | O()s
def domino_piling(m, n):
    horizontal = n // 2
    horizontal *= m
    if n % 2 == 1:
        horizontal += (m//2)
    print(horizontal)
    
m, n = input().split(' ')
m, n = int(m), int(n)
domino_piling(m, n)

# domino_piling(2, 4)
# domino_piling(3, 3)
# domino_piling(2, 1)
# domino_piling(2, 1)

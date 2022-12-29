# https://codeforces.com/problemset/problem/4/A
#  O()t | O()s
def watermelon(n):
    if n<=2 or n % 2 != 0:
        print("NO")
    else:
        print("YES")
    
    
n = int(input())
watermelon(n)

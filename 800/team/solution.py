# https://codeforces.com/problemset/problem/231/A Team
#  O()t | O()s
n = int(input())
total = 0
for i in range(n):
    array = input().split(" ")
    sure = 0
    for val in array:
        if val == "1":
            sure +=1
    if sure >= 2:
        total +=1
print(total)

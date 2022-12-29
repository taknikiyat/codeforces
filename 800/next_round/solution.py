# https://codeforces.com/problemset/problem/158/A
# O()t | O()s
def next_round(n, k, array):
    total = 0
    for i in range(k):
        if array[i] > 0: total += 1
    if array[k - 1] == 0:
        print(total); return
    i = k
    while(i < len(array)):
        if array[i] >= array[k - 1] and array[i] > 0:
            total += 1
        else:
            break
        i += 1
    print(total)
    
n, k = input().split(' ')
n, k = int(n), int(k)
array = input().split(" ")
array = [int(val) for val in array]
next_round(n, k, array)

# next_round(8, 5, array= [10, 9, 8, 7, 7, 7, 5, 5])
# next_round(8, 5, array= [10, 9, 8, 7, 0, 0, 0, 0])
# next_round(4, 2, array= [0, 0, 0, 0])

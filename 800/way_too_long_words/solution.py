# https://codeforces.com/problemset/problem/71/A
#  O()t | O()s 
def way_too_long_words(word):
    if len(word) <= 10:
        print(word)
        return
    print(word[0] + str(len(word) - 2) + word[-1])

n = int(input())
for i in range(n):
    word = input()
    way_too_long_words(word)

import sys

input = lambda : sys.stdin.readline().rstrip()
current, price = [int(num) for num in input().split()]
total = current + (price // 50)
point = (price // 50)
get = 0
if total >= 10:
    get += 1
print("%d" % total)
print("%d" % point)
print("%d" % get)
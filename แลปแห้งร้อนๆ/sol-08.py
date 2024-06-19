import sys

input = lambda : sys.stdin.readline().rstrip()

start, price = [int(num) for num in input().split()]
profit = price - (price * 0.07) - (start * 1.03)
print("%.1f" % profit)
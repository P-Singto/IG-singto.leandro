import sys

input = lambda : sys.stdin.readline().rstrip()

X, Y = [float(num) for num in input().split()]
print("%.2f" % (X * Y * 12))
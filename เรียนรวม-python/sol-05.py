import sys

input = lambda : sys.stdin.readline().rstrip()
speed = float(input())
distance = int(input())
time = (distance * (10 ** 6) / speed) / (60 * 60 * 24)
print("%.2f" % time)
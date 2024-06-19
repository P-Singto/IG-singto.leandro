import sys

input = lambda : sys.stdin.readline().rstrip()
voltage = float(input())
capasity = float(input())
usage = float(input())
print("%.1f" % (voltage * capasity / usage))
import sys

input = lambda : sys.stdin.readline().rstrip()
m_HR = float(input())
HR = m_HR - 20
print("%d" % (HR * 0.6))
print("%d" % (HR * 0.7))
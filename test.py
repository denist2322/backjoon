import sys

input = sys.stdin.readline

N = input()
result = ""

repoNum = []
for i in range(len(N)-1):
    repoNum.append(int(N[i]))

repoSortedNum = sorted(repoNum, reverse=True)

for i in repoSortedNum:
    result += str(i)

print(result)

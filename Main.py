import sys
input = sys.stdin.readline

N = int(input())
num = sorted([int(input())for _ in range(N)])

# 산술평균
avg = sum(num)/N
if -1 < avg < 0:
    print(0)
else:
    print(round(avg))
# 중앙값
midValue = num[N//2]
if -1 < midValue < 0:
    print(0)
else:
    print(midValue)

# 최빈값
max = 0
arr = [-1]*8001
cnt = 0
arr_repo = []
find_max = 0

if(len(num) == 1):
    print(num[0])
else:
    for i in num:
        arr[i+4000] += 1

    for i in range(8001):
        if(arr[i] > find_max):
            arr_repo.clear()
            cnt = 0
            find_max = arr[i]
            max = i-4000
            arr_repo.append(max)
            continue

        if(arr[i] == find_max):
            cnt += 1
            arr_repo.append(i-4000)
            continue

    if(cnt >= 1):
        print(sorted(arr_repo)[1])  # 최빈값 여러개면 두번째로 작은 수
    else:
        print(max)

# 범위
print(num[len(num)-1]-num[0])

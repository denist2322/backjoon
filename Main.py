n = int(input())

result = ""


def draw_star(n):
    global result
    # n이 1일때 = n이 더이상 3으로 나눠질 수 없을 때
    if n == 1:
        return ["*"]
    # n이 1이 될때 까지 실행
    stars = draw_star(n//3)

    for first in stars:
        result += first*3

    for second in stars:
        result += second + " "*(n//3) + second

    for third in stars:
        result += third*3


print(draw_star(n))

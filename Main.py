n = int(input())


def draw_star(n):
    # n이 1일때 = n이 더이상 3으로 나눠질 수 없을 때
    if n == 1:
        return ["*"]
    # n이 1이 될때 까지 실행
    stars = draw_star(n//3)
    print("stars :", n, stars)
    result = []
    # 3n + 1번째 줄
    for first in stars:
        result.append(first*3)
    # 3n + 2번째 줄
    for second in stars:
        result.append(second + " "*(n//3) + second)
    # 3n + 3번째 줄
    for third in stars:
        result.append(third*3)
    print("result:", n, result)
    return result


draw_star(n)
# print("\n".join(draw_star(n)))

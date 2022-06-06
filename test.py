n = int(input())


def draw_star(n):
    if n == 1:
        return ["*"]
    stars = draw_star(n//3)
    box = []
    for row in stars:
        box.append(row*3)
    for row in stars:
        box.append(row+' '*(n//3)+row)
    for row in stars:
        box.append(row*3)
    return box


print('\n'.join(draw_star(n)))

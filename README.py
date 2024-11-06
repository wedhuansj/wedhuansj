X, Y, H = map(int, input().split())
count = 0
current_height = 0
while current_height < H:
    count += 1
    current_height += X
    if current_height >= H:
        break
    current_height -= Y
print(count)

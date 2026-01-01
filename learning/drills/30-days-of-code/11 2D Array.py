
arr = []
for _ in range(6):

    row = list(map(int, input().split()))
    arr.append(row)


max_sum = -float('inf')


for i in range(4):
    for j in range(4):
        hourglass_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        )

        if hourglass_sum > max_sum:
            max_sum = hourglass_sum

print(max_sum)
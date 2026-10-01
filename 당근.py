T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    counts = 1
    max_counts = 0
    for i in range(0, N - 1):
        if nums[i] < nums[i + 1]:
            counts += 1
        else:
            counts = 1

        if counts > max_counts:
            max_counts = counts
    print(f"#{tc} {max_counts}")
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    all_score = []


    for i in range(N):
        scores = list(map(int, input().split()))
        total = (scores[0] * (35/100) + scores[1] * (45/100) + scores[2] * (20/100))
        all_score.append(total)
        if i == K-1:
            nums = total
    all_score.sort(reverse = True)

    rank = all_score.index(nums)

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    id = rank // (N // 10)

    print(f"#{tc} {grade[id]}")


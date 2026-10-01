# 테스트 개수
T = int(input())

# 테스트 반복
for tc in range(1, T+1):
    # 자연수 개수
    N = int(input())
    # 자연수 나열, 리스트로 만들어서 인덱싱하기
    text = list(map(int,input().split()))

    # 점수 세기
    scores = 0
    # 바로 오른쪽이랑 비교함
    # N으로 설정하면 N 다음은 없기 때문에 N-1까지 설정
    for i in range(N-1):
        # 왼쪽이 오른쪽보다 크다면 scores + 1
        if text[i] > text[i+1]:
            scores += 1
    answer = 0
    # 숫자들이 작아지면 scores 갯수는 N-1과 같아진다.
    # 출력을 1, 0으로 해야 하니까
    # scores가 만약 N-1이랑 같다면 1, 틀리면 0
    if scores == N-1:
        answer = 1
    else:
        answer = 0

    # 출력
    print(f"#{tc} {answer}")
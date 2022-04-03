T = int(input())
for t in range(1, T+1):
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    max_straight = 0
    for i in range(N):
        if S[i] > max_straight:
            max_straight += 1
    print("Case #{}: {}".format(t, max_straight))
T = int(input())
for i in range(T):
    C1, M1, Y1, K1 = map(int, input().split())
    C2, M2, Y2, K2 = map(int, input().split())
    C3, M3, Y3, K3 = map(int, input().split())
    min_c = min(C1, C2, C3)
    min_m = min(M1, M2, M3)
    min_y = min(Y1, Y2, Y3)
    min_k = min(K1, K2, K3)
    if min_c + min_m + min_y + min_k < 1000000:
        print("Case #{}: IMPOSSIBLE".format(i+1))
    else:
        c = min_c
        m = min_m
        y = min_y
        k = min_k
        while c + m + y + k > 1000000:
            diff = c + m + y + k - 1000000
            if diff > 0:
                if c > 0:
                    if c - diff < 0:
                        diff -= c
                        c = 0
                    else:
                        c -= diff
                        diff = 0
                if m > 0:
                    if m - diff < 0:
                        diff -= m
                        m = 0
                    else:
                        m -= diff
                        diff = 0
                if y > 0:
                    if y - diff < 0:
                        diff -= y
                        y = 0
                    else:
                        y -= diff
                        diff = 0
                if k > 0:
                    if k - diff < 0:
                        diff -= k
                        k = 0
                    else:
                        k -= diff
                        diff = 0
        print("Case #{}: {} {} {} {}".format(i+1, c, m, y, k))
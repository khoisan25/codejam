T = int(input())
for t in range(1, T + 1):
    R, C = [int(s) for s in input().split(" ")]
    print("Case #{}:".format(t))
    print(".." + "+-" * (C - 1) + "+")
    print(".." + "|." * (C - 1) + "|")
    print("+-" * (C) + "+")
    for row in range(R - 2):
        print("|." * (C) + "|")
        print("+-" * (C) + "+")
    print("|." * (C) + "|")
    print("+-" * (C) + "+")
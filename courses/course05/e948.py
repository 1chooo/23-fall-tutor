times = int(input())

for i in range(times):
    G, A, H, W = map(int, input().split())

    if G == 1:
        BMR = 13.7 * W + 5.0 * H - 6.8 * A + 66
    else:
        BMR = 9.6 * W + 1.8 * H - 4.7 * A + 655

    print(f"{BMR:.2f}")

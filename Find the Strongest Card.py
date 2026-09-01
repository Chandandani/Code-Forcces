while True:
    n = int(input())
    if n == 0:
        break

    cards = list(map(int, input().split()))

    best = cards[0]
    for c in cards:
        if c == 2:
            best = 2
            break
        if c == 1:
            if best != 2:
                best = 1
        elif best not in (1, 2):
            if c > best:
                best = c

    print(best)
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    words = [input().strip() for _ in range(n)]
    abbreviations = [input().strip() for _ in range(m)]

    
    available = set(word[0].upper() for word in words)

    remaining = abbreviations[:]

    while True:
        new_remaining = []
        changed = False

        for abbr in remaining:
           
            if all(ch in available for ch in abbr):
                
                if abbr[0] not in available:
                    available.add(abbr[0])
                    changed = True
            else:
                new_remaining.append(abbr)

        remaining = new_remaining

        
        if not changed: 
            break

    if not remaining:
        print("YES")
    else:
        print("NO")
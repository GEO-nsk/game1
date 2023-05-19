count = 0
for s in range(1, 10):
        for e in range(10):
            if e == s:
                continue
            for n in range(10):
                if n == e or n == s:
                    continue
                for d in range(10):
                    if d == s or d == e or d == n:
                        continue
                    for m in range(1, 10):
                        if m == e or m == n or m == s:
                            continue
                        for o in range(10):
                            if o == m or o == e or o == n or o == s:
                                continue
                            for r in range(10):
                                if r == m or r == o or r == e or r == n or r == s:
                                    continue
                                for y in range(10):
                                    if y == s or y == e or y == n or y == d or y == m or y == o or y == r:
                                        continue
                                    if ((1000*s + 100*e + 10*n + d) + (1000*m + 100*o + 10*r + e)) == \
                                            (10000*m + 1000*o + 100*n + 10*e + y):
                                        count += 1

print(count)

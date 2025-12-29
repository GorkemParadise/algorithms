from bisect import bisect_right
from collections import Counter

def possible_wins(M, B):
    M_sorted = sorted(M)
    B_sorted = sorted(B)
    i = j = wins = 0
    n = len(M_sorted)
    while i < n and j < n:
        if B_sorted[j] > M_sorted[i]:
            wins += 1
            i += 1
            j += 1
        else:
            j += 1
    return wins

def solve():
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    M = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxWins = possible_wins(M, B)

    mult = Counter(B)
    result = []
    total_wins = 0

    for i in range(N):
        candidates = sorted(mult.keys(), reverse=True)

        placed = False
        for v in candidates:
            mult[v] -= 1
            if mult[v] == 0:
                mult.pop(v)

            this_win = 1 if v > M[i] else 0

            future_B = []
            for val, cnt in mult.items():
                future_B.extend([val] * cnt)

            future_M = M[i+1:]
            future_wins = this_win + possible_wins(future_M, future_B)

            if total_wins + future_wins == maxWins:
                result.append(v)
                total_wins += this_win
                placed = True
                break
            else:
                mult[v] = mult.get(v, 0) + 1

        assert placed, "Should always place something"
    print(*result)

if __name__ == "__main__":
    solve()

import sys
input = sys.stdin.readline
MOD = 998244353
MAX = 200000 + 5

# factorials
fact = [1] * MAX
for i in range(2, MAX):
    fact[i] = fact[i-1] * i % MOD


def coord_pairwise_sum(arr):
    arr.sort()
    n = len(arr)
    total = 0
    # formula: sum_{k=0..n-1} arr[k] * (2*k - n + 1)
    for k, val in enumerate(arr):
        total += val * (2*k - n + 1)
    return total * 2   # because sum_{i!=j} |xi - xj| = 2 * sum_{i<j}


T = int(input())
for _ in range(T):
    N = int(input())
    X, Y, Z = [], [], []
    for _ in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)

    # ===== MEDIAN part =====
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    Z_sorted = sorted(Z)

    mx = X_sorted[N//2]
    my = Y_sorted[N//2]
    mz = Z_sorted[N//2]

    total_to_median = 0
    for i in range(N):
        total_to_median += abs(X[i] - mx) + abs(Y[i] - my) + abs(Z[i] - mz)

    # ===== PAIRWISE part: O(N log N) =====
    pair_x = coord_pairwise_sum(X_sorted.copy())
    pair_y = coord_pairwise_sum(Y_sorted.copy())
    pair_z = coord_pairwise_sum(Z_sorted.copy())
    total_pair = pair_x + pair_y + pair_z

    # ===== final =====
    ans = fact[N-1] * ((total_to_median + total_pair) % MOD) % MOD
    print(ans)

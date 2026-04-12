import sys

def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AA = A[0]
    BB = B[0]

    for i in range(1, n):
        AAA = min(AA, BB + k) + A[i]
        BBB = min(BB, AA + k) + B[i]
        AA, BB = AAA, BBB

    print(min(AA, BB))

if __name__ == "__main__":
    main()
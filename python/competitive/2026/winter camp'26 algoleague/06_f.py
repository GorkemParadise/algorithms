import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])

    if n == 1:
        print("YES")
    elif n == 2 or n == 3:
        print("NO")
    elif n == 4:
        if k == 2 or k == 3:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

if __name__ == "main":
    solve()
def main():
    N = 6
    R = 2
    edges = [
        (1, 2),
        (3, 2),
        (2, 4),
        (5, 4),
        (6, 4)
    ]
    print(f"{N} {R}")
    for a, b in edges:
        print(a, b)

if __name__ == "__main__":
    main()
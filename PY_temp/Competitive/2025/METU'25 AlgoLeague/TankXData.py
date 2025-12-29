n, m = map(int, input().split())
s = input().strip()
t = input().strip()
lt = len(t)

stack = []

for ch in s:
    stack.append(ch)
    if len(stack) >= lt and stack[-lt:] == list(t):
        for _ in range(lt):
            stack.pop()

print(len(stack))

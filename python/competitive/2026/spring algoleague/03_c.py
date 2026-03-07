## HH : MM : SS 
## 00 <= HH <= 23
## 00 <= MM <= 59
## 00 <= SS <= 59
## T1 < T2
## Example input: 00:00:00 01:00:10

def clear(time):
    time = time.replace(":", "")
    return time == time[::-1]

T1, T2 = input().split()

h1, m1, s1 = map(int, T1.split(":"))
h2, m2, s2 = map(int, T2.split(":"))

count = 0

while True:
    if clear(f"{h1:02d}:{m1:02d}:{s1:02d}"):
        count += 1
    
    if h1 == h2 and m1 == m2 and s1 == s2:
        break
    
    s1 += 1
    if s1 == 60:
        s1 = 0
        m1 += 1
    if m1 == 60:
        m1 = 0
        h1 += 1
    if h1 == 24:
        h1 = 0

print(count)

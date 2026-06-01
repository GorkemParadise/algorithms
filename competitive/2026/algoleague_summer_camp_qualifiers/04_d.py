# TIME LIMIT YEDİM..

Q = int(input())
stream = {}

for _ in range(Q):
    line = input().split()
    t = line[0]

    if t == '1':
        stream[line[1]] = int(line[2])

    elif t == '2':
        if line[1] in stream:
            del stream[line[1]]

    elif t == '3':
        if not stream:
            print("None")
        else:
            en_cok = -1
            isim = ""
            for nick, count in stream.items():
                if count > en_cok or (count == en_cok and nick < isim):
                    en_cok = count
                    isim = nick
            print(isim)

    else:
        if len(stream) < 2:
            print(0)
        else:
            print(max(stream.values()) - min(stream.values()))

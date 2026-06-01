# Yikilan kule için: son vurustan once toplam hasar s olmali
# s >= H - d_son_kart (kuleyi yikacak kadar) ve s < H (daha once yikilmamis)
# Her son kart için bu aralikta f[s] toplanir

MOD = 10**9 + 7

d = list(map(int, input().split()))

# f[0] = 1, f[s] = sum(f[s-d_i]) her kart icin
max_s = 4423  # anıl sol kule için H-1
f = [0] * (max_s + 1)
f[0] = 1

for s in range(1, max_s + 1):
    for mehmetaga in d:
        if s >= mehmetaga:
            f[s] = (f[s] + f[s - mehmetaga]) % MOD

# berke: sol 3668-13=3655 hasar, sağ 3668-962=2706 hasar, ikisi de yıkılmadı
berke = f[3655] * f[2706] % MOD

# anil: sol kule yıktı, sağ kule 4424-86=4338 hasar
# yıkılan kule icin
egriyol = [0] * (max_s + 2)
for i in range(max_s + 1):
    egriyol[i + 1] = (egriyol[i] + f[i]) % MOD

H = 4424
anil_sol = 0
for di in d:
    dogru = max(0, H - di)
    egri = H - 1
    anil_sol = (anil_sol + egriyol[egri + 1] - egriyol[dogru]) % MOD

anil = anil_sol * f[4338] % MOD

# hayat bitti
# https://open.spotify.com/intl-tr/track/5mfIBJ0KnaJbnxpRqtbHgL?si=4367a5369ead47a3

print(berke)
print(anil)

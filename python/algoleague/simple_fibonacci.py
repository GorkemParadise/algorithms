from typing import List
import math

MOD = 10**9 + 7

n = int(input())
dp = [0]*(max(3,n+1))
dp[1]=dp[2]=1
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2])%MOD

print(dp[n])

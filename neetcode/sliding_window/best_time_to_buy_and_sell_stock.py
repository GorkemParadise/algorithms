"""
Problem: Best Time to Buy and Sell Stock
Link: https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150
Difficulty: Easy
"""


def bestTime(prices): 
    min_price = 100
    max_profit = 0
        
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

print(bestTime([7,1,5,3,6,4])) 
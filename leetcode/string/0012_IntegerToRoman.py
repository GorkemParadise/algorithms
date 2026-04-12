class Solution:
    def intToRoman(self, num: int) -> str:
        values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        total = 0

        out = ""
        for value, s in values:
            count = num // value
            out += s * count
            num %= value
        
        return out
    
sol = Solution()
ml = sol.intToRoman(58)
print(ml)

'''
Input: num = 58

Output: "LVIII"


Input: num = 1994

Output: "MCMXCIV"


Input: num = 3749

Output: "MMMDCCXLIX"
'''


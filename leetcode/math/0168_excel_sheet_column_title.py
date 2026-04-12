"""
Problem: 168. Excel Sheet Column Title
Link: https://leetcode.com/problems/excel-sheet-column-title/
Difficulty: Easy
"""



from typing import List

#######################################################
# Altarnetive solution with C, you can check it.#
#######################################################

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = {
            1: 'A', 
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z',
        }
        result = []

        while columnNumber > 0:
            mod = columnNumber % 26
            if mod == 0:
                result.append(alphabet[26])
                columnNumber = (columnNumber - 1) // 26
            else:
                result.append(alphabet[mod])
                columnNumber = (columnNumber - mod) // 26
        return ''.join(result[::-1])



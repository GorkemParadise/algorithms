class Solution():
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        
        for charter in s:
            count_s[charter] = count_s.get(charter, 0) + 1
        for charter in t:
            count_t[charter] = count_t.get(charter, 0) + 1
        return count_s == count_t
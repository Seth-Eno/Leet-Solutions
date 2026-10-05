class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True

        x = 0

        while len(t) > 0:
            subset_char = s[x]

            if t[0] == subset_char:
                x += 1
                t = t[1:]

            else:
                t = t[1:]
            
            if x == len(s):
                return True

        return False

# Solution: I built a crawler to go through t removing the first value each time, and if the first value matched the search charecter in s, it would look for the next charecter in s. If the charecter in x matched the length of s, the substring was complete and the return would be true. Otherwise, it would go through all of t and never match s, in which case s is not a substring of t.
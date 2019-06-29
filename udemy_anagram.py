# Program to check if two strings are anagrams

def anagram(s1, s2):
""" (str, str) -> bool
Return True if s1 and s2 are anagrams

>>> anagram(s1, s2)
True
"""
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    s1_new = list(s1)
    s2_new = list(s2)
        
    if len(s1_new) == len(s2_new):
        dupe_found = True
        while dupe_found:
            dupe_found = False
            for i in s1_new:
                for j in s2_new:
                    if i == j:
                        s1_new.remove(i)
                        s2_new.remove(j)
                        dupe_found = True
                        break
                break
    return s1_new == s2_new

s1 = "public relations"
s2 = "crap built on lies"

print(anagram(s1, s2))

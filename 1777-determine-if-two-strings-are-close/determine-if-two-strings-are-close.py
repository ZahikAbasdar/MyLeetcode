from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1, c2 = Counter(word1), Counter(word2)
        
        # Check if both have the same unique characters and frequency distribution
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
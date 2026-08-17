class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            last_pos[char] = i
            # The smallest index among 'a', 'b', and 'c' determines 
            # how many valid left-endpoints exist for a substring ending at index i
            count += 1 + min(last_pos['a'], last_pos['b'], last_pos['c'])
            
        return count
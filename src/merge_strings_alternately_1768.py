''' solution to leet code problem number 1768: Merge Strings Alternately '''

class Solution(object):
    '''    
        Prompt:
            You are given two strings word1 and word2. Merge the strings by 
            adding letters in alternating order, starting with word1. If a 
            string is longer than the other, append the additional letters 
            onto the end of the merged string.

        Constraints:
            1 <= word1.length, word2.length <= 100
            word1 and word2 consist of lowercase English letters.
    '''
    
    def zip_longest(self, s1 : str, s2 : str) -> tuple[str, str] :
        ''' 
            zips two strings together based on the longest iterable
            when the shorter of the two is exhausted, an empty string
            will be returned in it's place
        '''
        
        lmax = len(s1)
        rmax = len(s2)

        for i in range(max(lmax, rmax)):

            if i < lmax and i < rmax:
                yield s1[i], s2[i]
                continue
            
            if i < lmax:
                yield s1[i], ''
                continue

            yield '', s2[i]
                
    def mergeAlternately(self, word1 : str, word2 : str) -> str :
        ''' 
            merges two strings alternately, starting with word1, then word2 
            ie. 'abcd' and 'pqrs' would become 'apbqcrds'
        '''
        
        out_str = ''
        for c1, c2 in self.zip_longest(word1, word2):
            out_str += c1
            out_str += c2
        return out_str
    
if __name__ == '__main__':
    test = Solution()
    print(test.mergeAlternately('abcd', 'pq'))
    
        

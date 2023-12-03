class Solution:

    #Find the longest substring without repeating chars
    def lengthOfLongestSubstring(s):

        lookup_table = set()
        longest_len = 0
        for i in range(len(s)):

            lookup_table.add(s[i])

            for j in range(i+1,len(s)):
                if s[j] in lookup_table:
                    break
                else:
                    lookup_table.add(s[j])

            if len(lookup_table) > longest_len:
                longest_len = len(lookup_table)
            
            lookup_table = set()

        return longest_len
    
    '''
        Much faster than my actual solution, however this does not preserve word order if that would matter
    '''
    def max_substr(s):
        char_lookup = set()
        max_len,start_idx = 0,0

        for idx,char in enumerate(s):
            print(char_lookup)
            while char in char_lookup:
                char_lookup.remove(s[start_idx])
                start_idx+=1
            char_lookup.add(char)
            max_len = max(max_len,idx-start_idx + 1)
        return max_len
    
test_func = Solution.max_substr#getattr(Solution,'lengthOfLongestSubstring')

input_str = 'abcdabcbbefgds'
print(test_func(input_str))
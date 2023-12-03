class Solution():

    def longestPalindrome(s):    

        def brute_force(s):

            def _is_palindrome(substr):
                lidx,ridx = 0,len(substr)-1
                while lidx < ridx:
                    if substr[lidx] != substr[ridx]:
                        return False
                    lidx+=1
                    ridx-=1
                return True
            
            max_len = 0
            max_substr = ''

            total_iters = 0
            for i in range(len(s)):
                total_iters +=1
                for j in range(i,len(s)):
                    total_iters+=1
                    substr = s[i:j] if i!=j else s[i:]
                    str_len = len(substr)
                    if _is_palindrome(substr):
                        if str_len > max_len:
                            max_len = str_len
                            max_substr = substr
            return max_substr
        
        def center_expansion(substr):
            def _expand_center(s,l,r):
                while l >= 0 and r < len(substr):
                    if not s[l] == s[r]:
                        break
                    l-=1
                    r+=1
                return s[l+1:r]

            longest = ''
            
            for i in range(len(s)):
                p1 = _expand_center(s,i,i+1)
                p2 = _expand_center(s,i,i)
                longest = max([longest,p1,p2],key=len)

            return longest
        
        return center_expansion(s)
    



test_func = getattr(Solution,'longestPalindrome')
test_str = 'c' * 1000

print(test_func(test_str))
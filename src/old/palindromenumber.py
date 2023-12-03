class Solution:

    def isPalindrome(x):
        
        def is_palindrome(s):
            i,j = 0,len(s)-1
            while i <=  j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        if x < 0:
            return False
        
        s = str(x)

        return is_palindrome(s)


test_func = getattr(Solution,'isPalindrome')
test = 121

print(test_func(test))
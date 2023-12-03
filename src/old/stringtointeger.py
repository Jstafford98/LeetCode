class Solution:

    def myAtoi(s):
        
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signs = ['+','-']
        min_val = -2147483648
        max_val = 2147483647
        
        s = s.strip()
        if s == '':
            return 0
            
        hasSign = s[0] in signs
        s,sign = (s[1:],s[0]) if hasSign else (s,'')
        
        stopdex = len(s)
        for i,c in enumerate(s):
            if c not in digits:
                stopdex = i
                break
        s = sign + s[:stopdex]
        
        try:
            s = int(s)
        except:
            s = 0
            
        s = min_val if min_val >= s else s
        s = max_val if max_val <= s else s
        
        return s

test_func = getattr(Solution,'myAtoi')
print(test_func('+4573'))

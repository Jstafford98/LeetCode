class Solution:
    def reverse(x):

        integer = str(x)
        negative = integer[0] == '-'
        mindex = 0 if not negative else 1
        curr = len(integer)-1
        output = '' if not negative else '-'

        while curr >= mindex:
            output+= integer[curr]
            curr-=1
        output = int(output)
        '''
        output = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        '''
        mask = abs(output) & 0x7fffffff
        return output if abs(output) == mask else 0

test_func = getattr(Solution,'reverse')
test_input = 123 

print(test_func(test_input))
from pprint import pprint

class Solution:
    
    '''
        The general process for this is to iterate the string with a step equal to (numRows*2)-2. 
        This will mean each iteration we work with the full down column we zig with and the values 
        we step back up with in the zag. 

        In each iteration, pull all zig values and zag values into their own string then enumerate them,
        and add them to our matrix using the resultant indecies.

        At the end join all matrix values into a string
    
    '''
    def convert(s,numRows):
        
        #If only one row, just return input
        if numRows <= 1:
            return s

        matrix = {k:[] for k in range(numRows)}
        step = (numRows*2)-2
        zagcrament = step-numRows

        start = 0
        
        while start < len(s):

            zig_step = start + numRows
            zag_step = zig_step + zagcrament

            zigs = enumerate(s[start:zig_step],start=0)
            
            #The enum start here has to be checked incase the string ends mid zag up
            enum_start = 1 + (zagcrament - len(s[zig_step:zag_step]))
            zags = enumerate(reversed(s[zig_step:zag_step]),start=enum_start)

            #Add zigs then zags to our matrix
            for k,v in zigs:
                matrix[k] = matrix[k] + [v]

            for k,v in zags:
                matrix[k] = matrix[k] + [v]

            start += step

        return ''.join([''.join(x) for x in matrix.values()])


test_func = getattr(Solution,'convert')

tests = [
    ('PAYPALISHIRING',3,'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING',4,'PINALSIGYAHRPI'),
    ('ABCDE',4,'ABCED'),
    ('A',1,'A'),
    ('AB',1,'AB')
]

for test in tests:
    test_str,nrows,output = test
    result = test_func(test_str,nrows)
    passed = result == output
    print('------------------------------------')
    print(f'\tInput: {test_str}\n\tOutput: {result}\n\tExpected: {output}\n\tPassed: {passed}\n')

class Pattern:

    '''
        WILDCARD SEARCH:
            find last occurance of following definite string
        ANY:
            if has another definite after, look for first occurance of that 
        REPEATING:
            find next literal that doesn't match repeating char 
    '''
    def __init__(self,pattern):

        self.pattern = pattern

        self.pattern_set = set(self.pattern)
        self.special_chars = set(['.','*','.*'])
        self.compiled = False
        self.has_special = False

    def compile(self):
        self.compiled = True
        self.has_special = len(self.special_chars.intersection(self.pattern_set)) > 0
        self.pattern_literals  = []
        for pattern in self.pattern.split('.*'):
            sub_pats = pattern.split('*')
            self.pattern_literals.extend(sub_pats)

    def _wildcard(self,s,literal):
        window = len(literal)
        start = len(s)

        for i in range(start,0,-window):
            if s[i:window] == literal:
                return i
        return None
    
    def _repeat(self,s,pat):
        for i in range(len(s),0,-1):
            if s[i] == pat:
                return i+1
        return None

    def __next_literal(self):
        try:
            return self.pattern_literals.pop()
        except IndexError:
            return None
        
    def _match(self,s):

        str_loc = 0
        reg_loc = 0

        str_max = len(s)
        reg_max = len(self.pattern)

        if str_max == 0 and reg_max > 0:
            return False
        elif str_max == 0 and reg_max == 0:
            return True
        
        match = True
        while str_loc < str_max and reg_loc < reg_max:

            str_char = s[str_loc]
            pat_char = self.pattern[reg_loc]
            next_pat_char = self.pattern[reg_loc+1] if reg_loc < reg_max-1 else ''
            pat_char = pat_char + next_pat_char

            if pat_char == '.*':
                reg_loc += 2
                substr = s[str_loc:]
                nxt_ltrl = self.__next_literal()
                if not nxt_ltrl:
                    match = False
                    break

                str_loc = self._wildcard(substr,nxt_ltrl)

            elif pat_char == '*':
                reg_loc += 1
                substr = s[str_loc:]
                nxt_ltrl = self.__next_literal()
                if not nxt_ltrl:
                    match = False
                    break

                str_loc = self._repeat(substr,nxt_ltrl)

            else:
                if pat_char != '.' and pat_char != str_char:
                    match = False
                    break

                str_loc += 1
                reg_loc += 1
            
            if not str_loc:
                match  = False
                break
        
        return match
       
    def match(self,s):
        if not self.compiled:
            self.compile()
        
        if not self.has_special:
            return self.pattern == s
        
        else:
            return self._match(s)
        
p = Pattern('a.')
print(p.match('aa'))        

def check_balance(input_str):
    if len(s) < 2:
            return False
        
    stack = []
    opening_brkts = dict()
    opening_brkts['('] = ')'
    opening_brkts['['] = ']'
    opening_brkts['{'] = '}'
    opening_brkts['*'] = '-'
    stack.append('*')

    for char in s:
        temp = ''
        if char in opening_brkts:
            stack.append(char)
        else:
            temp = stack.pop()
            if char != opening_brkts[temp]:
                return False
                
    if len(stack) > 1:
        return False
        
    return True
  
  my_str, my_str2, my_str3 = '({[]})', '({[)]})', ''

print(check_balance(my_str))
print(check_balance(my_str2))
print(check_balance(my_str3))

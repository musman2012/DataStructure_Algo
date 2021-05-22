def repeating_chars(in_str):
    str_dict = dict()
    for char in in_str:
        if char in str_dict:
            return char
        else:
            str_dict[char] = char
    
    return '*'
  
my_str, str_2 = 'ASDFGHJKLMNBVCXZ', 'ASDFGHJKLAMNBVCXZ'
print(repeating_chars(my_str))
print(repeating_chars(str_2))

'''
Output:
*
A
'''

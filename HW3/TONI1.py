# RECURSIVE FUNCTIONS
# recursive 1
def replace_char(astr, old_char, new_char):
    """
    :param astr: string with word[s]
    :param old_char: character to be replaced
    :param new_char: character that replaces old_char
    :return:
    """
    if astr == '':  # once end of string is reached, exit function
        print("5")
        return ''
    if astr[0] == old_char:  # if astr == old_char, as
        print("2")
        return new_char + replace_char(astr[1:], old_char, new_char)
    # | This is the first return statement reached, the first letter in the string
    # V is replaced
    print("0", astr[0], astr)
    print("01", astr[1:])
    return astr[0] + replace_char(astr[1:], old_char, new_char)



print(replace_char("super duper", 'u', 'oo'))

# recursive 2

# def occurences(astr, substr):
#     if len(astr) == 0 or len(substr) == 0:
#         return 0
#     if astr()

# occurences("how now brown cow", 'ow')
# occurences("house mouse louse", 'ow')
# occurences("green eggs and ham", 'egg')

# recursive 3

def inverse_pair(L):
    if len(L) == 2: # base case
        if l[0] + L[-1] == 0: # check sum of first and last item == 0
            return True
        return False
    if len(L) > 2:  #first check without first item, then check without last item
        inverse_pair(L[1] + L[-1])
        return True
    else:
        inverse_pair(L[0] + L[-2])
        return True

# [5, 6, 7, -6, 4, 3]
# first check, the sum of the first item and last item. if the sum is == 0, return true
# two recursive calls, check list without first, check list without last
#


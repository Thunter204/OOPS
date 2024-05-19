"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 1, Homework 3
Object Oriented Programming (50:198:113), Spring 2022

Create 3 seperate recursive functions:
1)  Write a recursive function called replace char with two parameters: a string astr, a character old char, and another
 character new char. The function should return a string in which every occurrence of old char in astr is replaced with
 new char.
2) Write a recursive function called occurrences with two parameters: a string astr and another (nonempty) string
substr. The function returns the number of times the substring substr appears in the string astr.
3) Write a recursive function called inverse pair with a single parameter L, which is a list of integers. The function
returns True if L contains a pair of integers whose sum is zero and False otherwise. The base case occurs when the list
has exactly
two integers
"""


# def replace_char(astr, old_char, new_char):
#     """
#     :param astr: string with word[s]
#     :param old_char: character to be replaced
#     :param new_char: character that replaces old_char
#     replace a letter(old_char) in astr with a new letter(new_char). there are two recursive calls;
#     the first one reached is the last return statement, which continuously returns and iterates through
#     astr until astr[0] == old_char. at this point, new_char is returned in place of astr[0] and iteration is continued.
#     once end of astr is reach, an empty string is returned and the new string is printed
#     """
#     if astr == '':  # once end of string is reached, exit function
#         return ''
#     if astr[0] == old_char:  # once astr == old_char, new char is returned in place of astr(so that string in replaced)
#         return new_char + replace_char(astr[1:], old_char, new_char)
#     # | This is the first return statement reached, the first letter in the string
#     # V is returns and the string is iterated through until astr[0] == old_char
#     return astr[0] + replace_char(astr[1:], old_char, new_char)


def occurences(astr, substr):
    """
    :param astr: string with words
    :param substr: string with letters
    The purpose of this function is to check the number of occurrences of substr in astr.
    """
    x = len(substr)
    if len(astr) == 0:
        return 0
    if len(substr) == 0:
        return True
    if astr[0:x] == substr:  # whatever the length of the substring is, that many letters of astr will be check at once
        return 1 + occurences(astr[1:], substr)  # count is returned
    return occurences(astr[1:], substr)


# def inverse_pair(L):
#     """
#     :param L: list of numbers
#     base case: len(L) == 2. otherwise, len(L) > 2 lists are created from L: one containing everything but the first item
#     in L and one containing everything but the last item in L. first and last items in list are added, and if not equal
#     to 0, they become smaller until the two digits are found that sum to 0 (unless there aren't any digits that sum to
#     0).
#     """
#     if len(L) == 2:  # base case
#         return L[0] + L[-1] == 0  # check sum of first and last item == 0
#     if len(L) > 2:  # first check without first item, then check without last item
#         L1 = L[1:]  # everything but first item in L
#         L2 = L[:-1]  # everything but last item in L
#     if (L1[0] + L1[-1] == 0) or (L2[0] + L2[-1] == 0):
#         return True
#     else:
#         return inverse_pair(L1) or inverse_pair(L2)  # iterates

# Programmer: Toni Hunter
# RUID: 187009925
# Date: 01/26/2022
#
# File: problem3.py
#
# Program Description: Implement a function called int_to_text with a single parameter N, which is an integer between 0
# and 1000 (inclusive).  The function returns a string that is the English text equivalent of that integer.
#
#
#
# import random
# N = random.randint(1, 1000)
N = int(input("num: "))
print(N)


def int_to_text(N):
    oneS = {0: ' ', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
            9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
            16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    tenS = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
            9: 'Ninety'}
    if N == 0:
        print("Zero")
    if N == 100:
        print("One Hundred")
    if N == 1000:
        print("One Thousand")
    elif 1 <= N <= 19:
        print(oneS[N])
    elif 20 <= N <= 99:
        one = N % 10
        ten = N // 10
        print("{} {}".format(tenS[ten], oneS[one]))
    elif 100 <= N <= 999:
        one = N % 10
        remainder = N // 10  # hundreds, tens -> split
        ten = remainder % 10  # tens
        hun = remainder // 10  # hundreds()
        print("{} hundred {} {}".format(oneS[hun], tenS[ten], oneS[one]))


int_to_text(N)


# I1 + I2
# I1.__add__I2
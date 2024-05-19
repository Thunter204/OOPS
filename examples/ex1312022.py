# given the list of strings, create a dictionary with two keys: 'vowels', 'consonants'.
# the value associated with the key is he number of words that begin with v or c.

L = ['hello', 'def', 'oop', 'world']
d = {'v': 0, 'c': 0}  # d = {}


for i in L:
    if i[0] in "aeiouAEIOU":
        d['v'] += 1   # my_dict['v'] = my_dict.get('v', 0) + 1
    else:             # ^^ creates the key since v/c isn't already in d, then modifies the key value
        d['c'] += 1   # my_dict['c'] = my_dict.get('c', 0) + 1

print(d)
#
# # given a list, create a dictionary in which keys are a digit(0-9), the value is the number of integers
# # in the list whose fist digit is the corresponding key.

L = [1, 29, 42, 111, 93, 245, 312]
d = {}

for num in L:
    key = int(str(num)[0])   # converting to str, starts at first digit, converts to int
    d[key] = d.get(key, 0) + 1   # puts first digit in d, updates values
print(d)

somestr = " "
def longword(somestr):
    return  len(someword) > 7   # more compact than if/else

# (1) using for loop
for i in range(2, int(math.sqrt(n) + 1)):
   if n%i == 0:
       return false
return true

# # (2) list comprehension
# L = [i #for i in range(1, n +1) if n%i == 0]
# print(#L)
# even = [n for n in numbers if n % 2 == 0]
# print(even)
#
# L = ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']


D = {}
for astr in L:
    D[len(astr)] = D.get(len(astr),  0) + 1
    print(D)

d = {'odds': 0, 'evens': 0}
for i in range(L):
    if i%2 == 0:
        d['evens'] += 1
    else:
        d['odds'] += 1

# trace here
x = "green"


def f():
    x = "eggs"

    def n():
        x = "ham"
        print(x)

    n()
    print(x)


print(x)

f()

print("-")

y = "green"


def m():
    def n():
        y = "eggs"
        print(y, len(y))

    n()
    print(y)


print(y)

m()


# fraction
def gcd(a, b):
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:  # common divisor
            return i

#Euclid gcd algorithm
def gdc(x, y):
    if y == 0:
        return x
    else:
        return gdc(y, x%y)

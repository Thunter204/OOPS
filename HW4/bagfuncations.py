"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 3, Homework 4
Object Oriented Programming (50:198:113), Spring 2022

write some functions that have Bag objects as parameters or return values. The point of this exercise is to use a class
that is given. 5 implementations are asked to be made (remove_item, remove_repeats, mode, union, and intersection).
Descriptions are given in each implementation.
"""


from bag import Bag


def remove_item(B, item):
    """
    Deletes all occurrences of item in Bag
    """
    for i in range(B.count(item)):
        Bag.erase_one(B, item)


def remove_repeats(B):
    """
    removes items that have been repeated but keeps original item
    """
    for i in B.items():
        duplicates = B.count(i) - 1 #counter, -1 to keep original
        for j in range(duplicates):
            Bag.erase_one(B, i)


def mode(B):
    """
    Returns a list of items that occurred most in Bag
    """
    maxi = 0
    L = []
    for i in B.items():
        if (B.count(i)) > maxi:
            maxi = B.count(i)
    for i in B.items():
        if maxi == B.count(i):
            L.append(i)
    return L


def union(B1, B2):
    """
    Returns bag object containing items from B1 and B2
    """
    unb= Bag()
    for i in B2.items():
        B1.insert(i)
        for j in B1.items():
            unb.insert(j)
    return unb.items()


def intersection(B1, B2):
    """
    Returns bag object containing items that are common in B1 snd B2
    """
    interb = Bag()
    for i in B1.items():
        for j in B2.items():
            if i == j:
                print(i, j)
                interb.insert(i)
    return interb.items()
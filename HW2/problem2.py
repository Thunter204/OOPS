"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 2, Homework 2
Object Oriented Programming (50:198:113), Spring 2022

Create a program tracks the transactions of customers from a bank. balance.dat is the file containing customer info and
transactions and will be used to create a dictionary. This dictionary will be used throughout the program to keep track
of withdrawals, deposits, max deposits and max withdrawals. two files are created, transsummary.dat and newbalance.dat,
containing the summary of transactions for each account and containing new balance information, respectively.
"""

cdictionary = {}
my_list = []


def customer_dictionary(balfilename):
    """
    :param balfilename: customer account information, "balance.dat"
    :return: cdictionary = {accNum: [ssn, balance, deposit, withdrawal, maxdep, maxdraw]}

    function opens balfilename for reading, transfers information into cdictionary
    """
    balancefile = open(balfilename, "r")  # open file for reading
    balanceline = balancefile.read()  # reads all lines in file
    linelist = balanceline.splitlines()  # ['line1', 'line2',...]
    for item in linelist:
        itemspl = item.split()  # each item in linelist are split and put into their own list ['acc', 'ssn', 'money']
        my_list.append(itemspl)  # itemspl is appended to my_list [[]]
    print("list", my_list)
    for i in my_list:  # creates variables for every item in my_list and put these variables into my_dict
        key = i[1]
        SSN = i[0]
        balance = float(i[2])
        deposit = 0
        withdrawal = 0
        maxdep = 0
        maxdraw = 0
        cdictionary[key] = [SSN, balance, deposit, withdrawal, maxdep, maxdraw]  # accNum: [ssn, balance, deposit,
        #                                                                         withdrawal, maxdep, maxdraw]
    balancefile.close()
    # print("cus_dict", cdictionary)
    return cdictionary


trans_list = []
max_min_dict = {}


def update_customer_dictionary(cdictionary, transfilename):
    """
    :param cdictionary: dictionary returned from customer_dicitonary
    :param transfilename: transactions.dat, contains account numbers and their transactions
    this function opens transaction file for reading and uses it to caluclate/update cdictionary value[2], value[3],
    value[4] and value[5]
    """
    transfilename = open(transfilename, "r")  # open transfilename('transactions.dat') for reading
    transline = transfilename.read()
    translinelist = transline.splitlines()  # each line is a single string in a list['line 1', 'line 2']
    for item in translinelist:
        itemspl = item.split()  # splits the items in each line ['bank numb', 'trans amount']
        trans_list.append(itemspl)  # [['line', '1'] ['line', '2']]
    # print("trans", trans_list)
    # for i in trans_list:
    #     key = i[0]
    #     dep = 0
    #     max_min_dict[key] = [dep]
    #     print("mmm", max_min_dict)
    #     if key in max_min_dict:
    #         max_min_dict[key].extend(trans_list[i][1])
    # print("mm", max_min_dict)
    for i in trans_list:  # i == [[i], [i], ...]
        key = i[0]  # puts items in trans-list into {key, num(value)}
        num = float(i[1])  # draw/dep
        if key in cdictionary:
            if num > 0:
                cdictionary[key][2] += num  # update deposits
            else:
                cdictionary[key][3] += num  # update withdrawals
    # print("up_cus", cdictionary)
    transfilename.close()
    return cdictionary


def new_balance_files(cdictionary, summfilename, newbalfilename):
    """
    :param cdictionary: created in customer_dictionary()
    :param summfilename: transsummary.dat
    :param newbalfilename: newbalfile.dat

    Function formats new files -- transsumarry.dat and newbalfile.dat . Also calculates/updates interest and penalty
    rates for each customer
    """
    summfile = open(summfilename, 'w')  # open files for writing
    newbalfile = open(newbalfilename, 'w')
    summfile.write(
        '{:<7}{:<14}{:<9}{:<10}{:<14}{:<8}{:13}{:>7}{:>10}{:>11}'.format('ACCT#', 'SSN', 'PREVBAL', 'DEPOSITS',
                                                                         'WITHDRAWALS',
                                                                         'MAXDEP', 'MAXWDRAW', 'INTEREST', 'PENALTY',
                                                                         'NEWBAL' + '\n'))
    summfile.write('-' * 102 + '\n')
#    interest = 0
    penalty = 0
    for key, value in cdictionary.items():  # put cdict values in variables
        acc = key
        ssn = value[0]
        pbal = value[1]
        dep = value[2]
        draw = value[3]
        mxdep = 0
        mxdraw = 0
        newbal = (int(value[1]) + int(value[2]) + int(value[3]))
        print(newbal, end=" ")
        if newbal < 100:
            interest = 0
            penalty += 10
        elif newbal > 3000:
            interest = (newbal * 0.02)
            penalty = 0
        else:
            interest = 0
            penalty = 0
        summfile.write(
            str('{:<7}'.format(acc)) + str('{:>10}'.format(ssn)) + str('{:10.2f}'.format(pbal)) + str(
                '{:10.2f}'.format(dep)) +
            str('{:13.2f}'.format(draw)) + str('{:8.2f}'.format(mxdep)) + str('{:11.2f}'.format(mxdraw)) +
            str('{:13.2f}'.format(interest)) + str('{:8.2f}'.format(penalty)) + str('{:11.2f}'.format(newbal)) + '\n')
        newbalfile.write(str('{:<15}'.format(ssn)) + str('{:<5}'.format(acc)) + str('{:10.2f}'.format(newbal)) + '\n')


if __name__ == "__main__":
    print("Running the problem2 module (Bank Transactions problem)\n")
    cdict = customer_dictionary("balance.dat")
    update_customer_dictionary(cdict, "transactions.dat")
    new_balance_files(cdict, "transsummary.dat", "newbalance.dat")
    print("Updated bank balance data appears in the files transsummary.dat and newbalance.dat")
    print("Goodbye!\n")

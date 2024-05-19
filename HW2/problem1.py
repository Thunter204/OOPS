"""
Author: Toni Hunter
RUID: 187009925
Module for Problem 1, Homework 2
Object Oriented Programming (50:198:113), Spring 2022

Create a program that formats files by removing trailing/leading white spaces and new lines, writing the results to a *.neb
file. Then, Formats 60 characters on each from *_neb.txt file and writes the results to *_final.txt. Finally, writes
number of non-blank lines, words, and average to *_stats.txt. outputs to user that stats and final have been created.
"""


def remove_extra_whitespaces(infile, outfile):
    """
    :param infile: user input file
    :param outfile: returned result: all extra white spaces removed
    : All white spaces such as extra new lines, consecutive spaces between words/beginning
    of lines and in between paragraphs. 1 space between paragraphs are kept. results written to outfile
    """
    infile = open(infile, "r")  # open for reading
    outfile = open(outfile, "w")  # open new file for writing
    rd_lns = infile.readlines()  # puts each line in list
    for i in rd_lns:
        if i == '\n':
            rd_lns.remove(i)  # SHOULD remove \n
        new = (" ".join(i.split()))  # joins strings
        outfile.write(new)
    infile.close()
    outfile.close()
    return outfile


def adjust_linelength(infile, outfile):
    """
    :param infile: essay_neb.txt
    :param outfile: essay_final.txt == essay_neb.txt len(lines) == 60
    :return:
    """
    infile = open(infile, 'r')
    outfile = open(outfile, 'w')
    rd = infile.readlines()
    for line in rd:
        frmttd_ln = ''
        wrd_cnt = 0
        for word in line.split():
            if len(word + ' ') <= 60:
                frmttd_ln = frmttd_ln + word + ' '
                wrd_cnt += len(word)
            else:
                frmttd_ln = frmttd_ln + '\n' + word + ' '
                wrd_cnt = 0
                wrd_cnt += len(word)
    outfile.write(frmttd_ln)


def essay_statistics(infile, outfile):
    """
     :param infile: essay_final.txt
     :param outifile: essay_stats.txt == # of non-blank lines, words, and average
     word length
     :return: essay_stats.txt
     """
    infile = open(infile, 'r')
    outfile = open(outfile, 'w')
    nonb_ln = 0
    num_wrd = 0
    wrd_Len = 0
    avg_Len = 0
    for line in infile:
        if line != '\n':
            nonb_ln += 1
            num_wrd += len(line.split())
            for words in line.split():
                wrd_Len = wrd_Len + len(words)
    avg_Len = wrd_Len / num_wrd
    outfile.write("Number of (non_blank lines: {}".format(nonb_ln) + '\n' + "Number of words: {}".format(num_wrd) +
                  '\n' + "Average word length: {}".format(int(avg_Len)))


def format_essay():
    """
    calls all functions and outputs to user that *_final.txt and *_stats.txt are created
    """
    print("Essay Formatting Helper Program")
    print('-' * 31)
    print()
    infile = input("Enter the name (*.txt) of the file containing the essay: ")
    print()
    outfile = '{}_neb.txt'.format(infile.replace('.txt', ''))  # these three files to be created
    noutfile = '{}_final.txt'.format(infile.replace('.txt', ''))
    nnoutfile = '{}_stats.txt'.format(infile.replace('.txt', ''))
    remove_extra_whitespaces(infile, outfile)
    adjust_linelength(outfile, noutfile)
    print("The formatted essay is in the file {}_final.txt".format(infile.replace('.txt', '')))
    essay_statistics(noutfile, nnoutfile)
    print("The essay statstics are in the file {}_stats.txt".format(infile.replace('.txt', '')))


if __name__ == '__main__':
    format_essay()

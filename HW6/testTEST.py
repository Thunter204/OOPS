def wordlengthAve(infilename, outfilename):
    try:
        ifile = open(infilename, 'r')
        ofile = open(outfilename, 'w')
        wlist = ifile.read().split()
        wordsL = [len(w) for w in wlist]
        ave = sum(wordsL) / len(wordsL)
    except ZeroDivisionError as e:
        print(e)
    else:
        ofile.write("{} {}".format(sum(wordsL, ave)))
    finally:
        ifile.close()
        ofile.close()


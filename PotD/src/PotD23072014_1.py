__author__ = 'alina'

def nParts(mystring, n):
    '''
    Divide a string in N equal parts
    :param mystring: input string
    :param n: number of parts
    :return:nothing
    '''
    len = mystring.__len__()

    if len % n != 0:
        print mystring, " does not contain ", n, " parts."
        return

    div = len // n
    for i, c in enumerate(mystring):
        if i % div == 0:
            print "\n"
        print c

if __name__ == "__main__":
    mystring = "testStringsollaris"
    nParts(mystring, 4)

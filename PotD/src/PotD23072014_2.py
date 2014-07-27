__author__ = 'alina'

def main(mystring):
    '''
    Returns the first character in a string that appears exactly one time.
    :param mystring: input string.
    :return:
    '''
    freqs = []
    chars = []

    for c in mystring:
        for i,ch in enumerate(chars):
            if c == ch:
                freqs[i] +=1
                break
        else:
            chars.append(c)
            freqs.append(1)

    for i, freq in enumerate(freqs):
        if freq == 1:
            print chars[i]
            break

if __name__ == "__main__":
    mystring = "perhonen"
    main(mystring)

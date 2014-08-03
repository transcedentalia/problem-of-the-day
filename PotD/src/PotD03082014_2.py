__author__ = 'alina'

def atoi(myString):
    if not myString:
        return None
    t = 0
    for i, ch in enumerate(reversed(myString)):
        t = pow(10, i) * int(ch) + t

    return t

if __name__ == "__main__":
    print atoi("123456789")

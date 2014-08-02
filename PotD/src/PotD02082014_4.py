__author__ = 'alina'

def isRotation(s1, s2):
    s2 = s2 * 2

    if s2.find(s1) != -1:
        return True
    return False


if __name__ == "__main__":
    s1  = bytearray("holidays")
    s2 = bytearray("daysholi")

    print isRotation(s1, s2)
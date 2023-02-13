from math import *
def is_surpassing_phrase(ch):
    t=ch.split()
    for i in range(len(t)):
        diff,prev=0,0
        for j in range(len(t[i])-1):
            diff =abs(ord(t[i][j])-ord(t[i][j+1]))
            if diff<prev:
                return False
            prev=diff
    return True
print(is_surpassing_phrase(""))

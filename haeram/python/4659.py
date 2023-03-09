from sys import stdin

vowel = ['a', 'e', 'i', 'o', 'u']

def isDouble(prev, cand):
    if(cand == prev and (cand != 'e' and cand != 'o')):
        # print('double', prev, cand, cand != 'e', cand != 'o')
        return True
    
    return False

while 1:
    str = stdin.readline().rstrip()
    if(str == 'end'):
        break

    vowelCnt = 0
    vowelCont = 0
    consoCont = 0
    prevWord = ''
    flag = True

    for s in str:
        if(isDouble(prevWord, s)):
            flag = False
            break

        if(s in vowel):
            vowelCnt += 1
            consoCont = 0
            if(vowelCont >= 2):
                flag = False
                break

            vowelCont += 1
        else:
            vowelCont = 0
            if(consoCont >= 2):
                flag = False
                break

            consoCont += 1

        prevWord = s

    if(flag and vowelCnt>0):
        print(f'<{str}> is acceptable.')
    else:
        print(f'<{str}> is not acceptable.')





        

        
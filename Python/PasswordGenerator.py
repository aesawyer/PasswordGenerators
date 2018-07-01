import random
import os
import sys

def main():
    print('Password Generator - Python Implementation')
    print('--------------------------------------------')
    print('How long would you like the password?')
    lenCheck = passLength()
    print('Upper-Case Letters? (Yes = 0, No = 1)')
    upCheck = BoolCheck()
    print('Numbers? (Yes = 0, No = 1)')
    numCheck = BoolCheck()
    print('Special Characters? (Yes = 0, No = 1)')
    specCheck = BoolCheck()
    print('Your randomly generated password is:')
    finalPass = Generate(lenCheck, upCheck, numCheck, specCheck)
    print('~~~~~~~~~~~~~~~~~~~~~~')
    print(finalPass)
    print('~~~~~~~~~~~~~~~~~~~~~~')
    print('Generate another password? (Yes = 0, No = 1)')
    genAgain = BoolCheck()
    restartProg(genAgain)

def passLength():
    passlen = None
    while not passlen:
        unchecked = input()
        try:
            passlen = int(unchecked)
            if passlen < 6:
                passlen = None
                print('    Invalid Entry. Password must be at least 6 characters in length')
            else:
                return passlen
        except ValueError:
            print('    You must enter a number')

def BoolCheck():
    upCheck = None
    while not upCheck:
        boolCheck = input()
        try:
            upCheck = int(boolCheck)
            if upCheck == 0 or upCheck == 1:
                return upCheck
            else:
                upCheck = None
                print('    You must enter 0 for Yes or 1 for No')
        except ValueError:
            print('    You must enter True or False')

def Generate(length, upCheck, numCheck, specCheck):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphUp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = ['0','1','2','3','4','5','6','7','8','9']
    spec = ['!','@','#','$','%','^','&','*',')','(','}','{','>','<','?']
    if upCheck == 0:
        alph.extend(alphUp)
    if numCheck == 0:
        alph.extend(num)
    if specCheck == 0:
        alph.extend(spec)
    charList = []
    while len(charList) < length:
        charList.extend(random.choice(alph))
    wordToPass = ''.join(charList)
    return wordToPass

def restartProg(genAgain):
    if genAgain == 0:
        os.system('cls')
        main()
    else:
        sys.exit()

main()

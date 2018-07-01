import random
import os
import sys

def Main():
    print('Password Generator - Python Implementation')
    print('--------------------------------------------')
    lenCheck = PassLength('How long would you like the password: ')
    upCheck = BoolCheck('Upper-Case Letters? (Yes = 0, No = 1): ')
    numCheck = BoolCheck('Numbers? (Yes = 0, No = 1): ')
    specCheck = BoolCheck('Special Characters? (Yes = 0, No = 1): ')
    Generate(lenCheck, upCheck, numCheck, specCheck)
    genAgain = BoolCheck('Generate another password? (Yes = 0, No = 1): ')
    RestartProg(genAgain)

def PassLength(inputSentence):
    passlen = None
    while not passlen:
        unchecked = input(inputSentence)
        try:
            passlen = int(unchecked)
            if passlen < 6:
                passlen = None
                print('    Password must be at least 6 characters in length')
            else:
                return passlen
        except ValueError:
            print('    You must enter a number')

def BoolCheck(inputSentence):
    upCheck = None
    while not upCheck:
        boolCheck = input(inputSentence)
        try:
            upCheck = int(boolCheck)
            if upCheck == 0 or upCheck == 1:
                return upCheck
            else:
                upCheck = None
                print('    You must enter 0 for Yes or 1 for No')
        except ValueError:
            print('    You must enter 0 for Yes or 1 for No')

def Generate(passlen, upCheck, numCheck, specCheck):
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
    while len(charList) < passlen:
        charList.extend(random.choice(alph))
    finalPass = ''.join(charList)
    print('Your randomly generated password is:')
    print('~~~~~~~~~~~~~~~~~~~~~~')
    print(finalPass)
    print('~~~~~~~~~~~~~~~~~~~~~~')

def RestartProg(genAgain):
    if genAgain == 0:
        os.system('cls')
        Main()
    else:
        sys.exit()

Main()

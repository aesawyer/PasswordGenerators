import random
import os
import sys

alph = ['abcdefghijklmnopqrstuvwxyz']
num = [0,1,2,3,4,5,6,7,8,9]
spec = ['!@#$%^&*(){}<>?']

def main():
    print('Password Generator - Python Implementation')
    print('--------------------------------------------')
    print('How long would you like the password?')
    passlen = passLength()
    print('passlen: ' + str(passlen))
    print('Upper-Case Letters? (True, False)')
    upCheck = BoolCheck()
    print(upCheck)

def passLength():
    len = sys.stdin.readline()
    try:
        len = int(len)
    except ValueError:
        print('    Must enter a number')
        len = None
        passLength()
    len = int(len)
    if len < 6:
        print('    Invalid Entry. Password must be at least 6 characters in length')
        passLength()
    else:
        return len

def BoolCheck():
    upCheck = sys.stdin.readline()
    try:
        upCheck == 'True'
    except ValueError:
        print('    Must enter True or False')
        BookCheck()
    return upCheck

main()

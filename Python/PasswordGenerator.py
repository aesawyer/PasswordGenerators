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
    lenCheck = passLength()
    print('Upper-Case Letters? (True, False)')
    upCheck = BoolCheck()
    print(upCheck)

def passLength():
    passlen = None
    while not passlen:
        unchecked = input()
        try:
            passlen = int(unchecked)
            if passlen < 6:
                passlen = None
                print('    Invalid Entry. Password must be at least 6 characters in length')
        except ValueError:
            print('    You must enter a number')

def BoolCheck():
    upCheck = sys.stdin.readline()
    try:
        upCheck == 'True'
    except ValueError:
        print('    Must enter True or False')
        BookCheck()
    return upCheck

main()

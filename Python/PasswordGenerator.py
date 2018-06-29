import random
import os
import sys

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = [0,1,2,3,4,5,6,7,8,9]
spec = ['!','@','#','$','%','^','&','*','(',')','{','}','<','>','?']

def main():
    print('Password Generator - Python Implementation')
    print('--------------------------------------------')
    print('How long would you like the password?')
    passlen = passLength()
    print('Password length is ')

def passLength():
    passlen = sys.stdin.readline()
    try:
        passlen = int(passlen)
    except ValueError:
        print('Must enter a number')
        passLength()
    if passlen < 6:
        print('Invalid Entry. Password must be at least 6 characters in length')
        passLength()
    else:
        return passlen

main()

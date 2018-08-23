#!/usr/bin/env python

def printAndReturnNothing():
    x = "hello"
    print(x)

def printAndReturn():
    x = "hello"
    print(x)
    return x

def main():
    ret = printAndReturn()
    other = printAndReturnNothing()

    print("ret is: %s" % ret)
    print("other is: %s" % other)

if __name__ == "__main__":
    main()
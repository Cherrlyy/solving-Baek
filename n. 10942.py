import sys

def isPalindromeNum() -> None:
    size = int(sys.stdin.readline())
    num = sys.stdin.readline().replace(" ", "")
    for i in range(int(sys.stdin.readline())):
        indexs = sys.stdin.readline().split()
        newNum = num[int(indexs[0])-1:int(indexs[1])]
        if newNum == newNum[::-1]:
            print("1")
        else:
            print("0")

isPalindromeNum()
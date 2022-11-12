# 10866 덱
import sys

def commandPopFront(result):
    try:
        print(result.pop(0))
    except:
        print("-1")

def commandPopBack(result):
    try:
        print(result.pop())
    except:
        print("-1")

def isEmpty(result):
    if result:
        print("0")
    else:
        print("1")

def commandFront(result):
    try:
        print(result[0])
    except:
        print("-1")

def commandBack(result):
    try:
        print(result[-1])
    except:
        print("-1")

commandList = []
result = []
tmp= []

N = int(sys.stdin.readline())
for i in range(N):
    commandList.append(input())

for i in range(len(commandList)):
    if commandList[i].find('push_back') != -1:
        tmp = commandList[i].split()
        result.append(tmp[1])
    if commandList[i].find('push_front') != -1:
        tmp = commandList[i].split()
        result.insert(0,tmp[1])
    if commandList[i] == 'front' != -1:
        commandFront(result)
    if commandList[i] == 'back' != -1:
        commandBack(result)
    if commandList[i].find('size') != -1:
        print(len(result))
    if commandList[i].find('empty') != -1:
        isEmpty(result)
    if commandList[i].find('pop_front') != -1:
        commandPopFront(result)
    if commandList[i].find('pop_back') != -1:
        commandPopBack(result)

# 10845 큐
import sys

def commandPop(result):
    try:
        print(result.pop(0))
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

N = int(sys.stdin.readline())
for i in range(N):
    commandList.append(input())

for i in range(len(commandList)):
    if commandList[i].find('push') != -1:
        tmp = commandList[i].split()
        result.append(tmp[1])
    if commandList[i].find('front') != -1:
        commandFront(result)
    if commandList[i].find('back') != -1:
        commandBack(result)
    if commandList[i].find('size') != -1:
        print(len(result))
    if commandList[i].find('empty') != -1:
        isEmpty(result)
    if commandList[i].find('pop') != -1:
        commandPop(result)


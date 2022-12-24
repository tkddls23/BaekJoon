from sys import stdin


while (1):
    try:
        cnt = 1
        now = 1
        n = int(stdin.readline())

        while True:
            if(now%n == 0):
                print(cnt)
                break
            else:
                cnt += 1
                now *= 10
                now += 1
    except:
        exit(0)
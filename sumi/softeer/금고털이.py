import sys
input = sys.stdin.readline

# https://softeer.ai/practice/info.do?idx=1&eid=395&sw_prbl_sbms_sn=128780


def main(w, arr):
    total = 0
    res = 0
    for m, price in arr:
        if total + m <= w:
            total += m
            res += m * price
        else:
            rest = w - total
            res += price * rest
            break

    return res


if __name__ == "__main__":
    w, n = map(int, input().split())

    arr = []
    for _ in range(n):
        r, c = map(int, input().split())
        arr.append((r, c))

    arr.sort(key=lambda x: x[1], reverse=True)
    res = main(w, arr)
    print(res)

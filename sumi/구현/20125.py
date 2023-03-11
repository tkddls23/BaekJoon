import sys

input = sys.stdin.readline


def solution(n, arr):
    def find_heart_pt():
        for i in range(n):
            for j in range(n):
                if arr[i][j] == '*':
                    return (i + 1, j)

    def find_left_arm(heart_pt):
        idx, jdx = heart_pt
        cnt = 0
        for j in range(jdx):
            if arr[idx][j] == '*':
                cnt += 1
        return cnt

    def find_right_arm(heart_pt):
        idx, jdx = heart_pt
        cnt = 0
        for j in range(jdx + 1, n):
            if arr[idx][j] == '*':
                cnt += 1
        return cnt

    def find_waist_pt(heart_pt):
        idx, jdx = heart_pt
        for i in range(idx + 1, n):
            if arr[i][jdx] != '*':
                return (i - 1, jdx)

    def find_left_leg(waist_pt):
        idx, jdx = waist_pt
        cnt = 0
        for i in range(idx + 1, n):
            if arr[i][jdx - 1] == '*':
                cnt += 1
        return cnt

    def find_right_leg(waist_pt):
        idx, jdx = waist_pt
        cnt = 0
        for i in range(idx + 1, n):
            if arr[i][jdx + 1] == '*':
                cnt += 1
        return cnt

    heart_pt = find_heart_pt()
    left_arm_cnt = find_left_arm(heart_pt)
    right_arm_cnt = find_right_arm(heart_pt)

    waist_pt = find_waist_pt(heart_pt)
    waist_cnt = waist_pt[0] - heart_pt[0]

    left_leg_cnt = find_left_leg(waist_pt)
    right_leg_cnt = find_right_leg(waist_pt)

    print(heart_pt[0] + 1, heart_pt[1] + 1)
    print(left_arm_cnt, right_arm_cnt, waist_cnt, left_leg_cnt, right_leg_cnt)


if __name__ == "__main__":
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    res = solution(n, arr)
    # print(res)

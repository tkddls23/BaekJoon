# https://freedeveloper.tistory.com/393 참고
def solution(sequence, k):
    n = len(sequence)
    start = 0
    end = 0
    seqSum = 0
    seqArr = []

    for start in range(n):
        while seqSum < k and end < n:
            seqSum += sequence[end]
            end += 1

        if seqSum == k:
            seqArr.append([start, end - 1])

        seqSum -= sequence[start]

    return sorted(seqArr, key=lambda seq: seq[1] - seq[0])[0]
function solution(a, b) {
    let answer = 0;

    let big, small;

    if (a > b) {
        big = a;
        small = b;
    } else {
        big = b;
        small = a;
    }

    for (let i = small; i <= big; i++) {
        answer += i;
    }

    return answer;
}

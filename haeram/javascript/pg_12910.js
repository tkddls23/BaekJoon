function solution(arr, divisor) {
    let answer = [];

    let cand = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % divisor === 0) {
            cand.push(arr[i]);
        }
    }

    if (cand.length === 0) {
        cand.push(-1);
    }

    answer = cand.sort((a, b) => a - b);
    return answer;
}

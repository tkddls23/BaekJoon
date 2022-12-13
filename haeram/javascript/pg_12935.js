function solution(arr) {
    let answer = [];

    if (arr.length <= 1) {
        return [-1];
    }

    const target = Math.min(...arr);
    answer = arr.filter((el) => el !== target);

    return answer;
}

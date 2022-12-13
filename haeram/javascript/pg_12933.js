function solution(n) {
    let answer = 0;

    let str = String(n);
    const splited = str.split("");

    splited.sort((a, b) => b - a);

    answer = Number(splited.join(""));

    return answer;
}

function solution(x) {
    let answer = true;

    const str = String(x);

    let total = 0;
    for (let i = 0; i < str.length; i++) {
        total += Number(str[i]);
    }

    if (x % total == 0) {
        answer = true;
    } else {
        answer = false;
    }

    return answer;
}

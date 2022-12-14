function solution(s) {
    let answer = -1;

    const stk = [];

    for (const it of s) {
        if (!stk.length) {
            stk.push(it);
            continue;
        }

        const lastData = stk.pop();
        if (lastData === it) {
            continue;
        } else {
            stk.push(lastData);
            stk.push(it);
        }
    }

    if (stk.length === 0) {
        answer = 1;
    } else {
        answer = 0;
    }

    return answer;
}
